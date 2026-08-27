from typing import Dict, Tuple

import torch

from core.const import MODEL_ICAO
from core.storage.utils import load_airport_info
from core.model.module import (
    ContinuousPositionalEncoding,
    TrajEncBlock,
    TrajDecBlock,
    TrajGen,
)


class TrajGen_Single(TrajGen):

    def __init__(
        self,
        #
        icao: str,
        #
        num_aircraft: int,
        #
        past_len: int,
        past_n_features: int,
        future_len: int,
        future_n_features: int,
        #
        d_model: int,
        nhead: int,
        widening_factor: int,
        enc_num_layers: int,
        dec_num_layers: int,
        #
        use_x_atten: bool,
        #
        dropout: float = 0.,
    ):
        super().__init__()

        self.use_x_atten = use_x_atten
        self.num_intent_embeddings = 4

        d_dec = past_n_features + d_model * (
            self.num_intent_embeddings + 2)

        # --- #

        self.c_pos_enc = ContinuousPositionalEncoding(
            d_dec if d_dec % 2 == 0 else d_dec + 1,
            dropout,
            d_dec,
        )

        #

        self.rwy_emb = torch.nn.Embedding(
            len(load_airport_info(icao)['runways_order']) + 1,
            d_model,
            padding_idx=0,
        )
        self.rwy_order_emb = torch.nn.Embedding(
            num_aircraft + 1,
            d_model,
            padding_idx=0,
        )
        self.is_ifr_emb = torch.nn.Embedding(
            2 + 1,
            d_model,
            padding_idx=0,
        )
        self.model_type_emb = torch.nn.Embedding(
            len(MODEL_ICAO) + 1,
            d_model,
            padding_idx=0,
        )

        #

        self.other_in_proj = torch.nn.Sequential(
            torch.nn.Linear(past_n_features, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, d_model),
        )
        self.enc_in_proj = torch.nn.Sequential(
            torch.nn.Linear(past_n_features, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, d_model),
        )

        self.dec_in_proj = torch.nn.Sequential(
            torch.nn.Linear(future_n_features, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, d_model),
        )
        self.out_proj = torch.nn.Sequential(
            torch.nn.Linear(d_model, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, future_n_features),
        )

        #

        self.o_enc = TrajEncBlock(
            num_aircraft * (self.num_intent_embeddings + 1),
            d_model,
            nhead,
            widening_factor,
            enc_num_layers,
            dropout=dropout,
        )
        self.enc = TrajEncBlock(
            self.num_intent_embeddings + past_len,
            d_model,
            nhead,
            widening_factor,
            enc_num_layers,
            dropout=dropout,
        )

        dec_cls = TrajDecBlock if self.use_x_atten else TrajEncBlock
        self.dec = dec_cls(
            future_len,
            d_model,
            nhead,
            widening_factor,
            dec_num_layers,
            dropout=dropout,
            cond_n_features=d_dec,
        )
        return

    def _forward_intent(
        self,
        intent_dict: Dict[str, torch.Tensor],
        mask: torch.Tensor,
    ):
        _rwy_emb = intent_dict['rwy_emb'].squeeze(dim=-1)
        _emb1 = self.rwy_emb(_rwy_emb)
        _emb1 = _emb1 * mask

        emb_list = [_emb1]

        # Stored landing order is zero-based, while zero is reserved for
        # padding in the embedding table.
        _rwy_order = intent_dict['rwy_order_emb'].squeeze(dim=-1) + 1
        valid = mask.squeeze(dim=-1).bool()
        _rwy_order = _rwy_order.masked_fill(~valid, 0)
        _order_emb = self.rwy_order_emb(_rwy_order)
        _order_emb = _order_emb * mask
        emb_list.append(_order_emb)

        _is_ifr_emb = intent_dict['is_ifr_emb'].squeeze(dim=-1)
        _emb2 = self.is_ifr_emb(_is_ifr_emb)
        _emb2 = _emb2 * mask
        emb_list.append(_emb2)

        _model_type_emb = intent_dict['model_type_emb'].squeeze(dim=-1)
        _emb3 = self.model_type_emb(_model_type_emb)
        _emb3 = _emb3 * mask
        emb_list.append(_emb3)

        _ego_emb = tuple(emb[:, 0:1] for emb in emb_list)
        ego_intent_emb = torch.cat(_ego_emb, dim=-2)
        intent_emb = torch.cat(emb_list, dim=-2)
        return ego_intent_emb, intent_emb

    def forward_encoder(
        self,
        #
        intent_dict: Dict[str, torch.Tensor],
        intent_mask: torch.Tensor,
        #
        other: torch.Tensor,
        other_mask: torch.Tensor,
        #
        src: torch.Tensor,
        src_padding_mask: torch.Tensor,
    ):
        """
        Args:
            intent_dict:      shape (B, S, 1)
            intent_mask:      shape (B, S)
            other:            shape (B, S, ?)
            other_mask:       shape (B, S)
            src:              shape (B, T1, ?)
            src_padding_mask: shape (B, T1)
        """
        # (B, S, D)
        mul_mask = (~intent_mask).float().unsqueeze(dim=-1)
        # (B, I, D), (B, I * S, D)
        ego_intent, intent = self._forward_intent(intent_dict, mul_mask)

        # (B, S, D)
        other_proj = self.other_in_proj(other)
        # (B, T, D)
        src_proj = self.enc_in_proj(src)

        # (B, S * (I + 1), D)
        o_src_tuple = (intent, other_proj)
        o_src = torch.cat(o_src_tuple, dim=-2)
        # (B, S * (I + 1))
        o_mask_tuple = (
            *([intent_mask] * self.num_intent_embeddings),
            other_mask,
        )
        o_mask = torch.cat(o_mask_tuple, dim=-1)

        # (B, I + T, D)
        _src_tuple = (ego_intent, src_proj)
        _src = torch.cat(_src_tuple, dim=-2)
        # (B, I + T)
        _mask = torch.nn.functional.pad(
            src_padding_mask,
            pad=(self.num_intent_embeddings, 0),
            mode='constant',
            value=False,
        )

        # (B, D), (B, S * (I + 1), D)
        o_cls_out, _ = self.o_enc(o_src, padding_mask=o_mask)

        # (B, D), (B, I + T, D)
        cls_out, src_out = self.enc(_src, padding_mask=_mask)

        # (B, ?)
        in_curr = src[..., -1, :]

        # (B, I * D)
        ego_intent_flat = ego_intent.flatten(start_dim=1, end_dim=2)
        # (B, ?)
        _ctx_tuple = (ego_intent_flat, in_curr, o_cls_out, cls_out)
        _ctx = torch.cat(_ctx_tuple, dim=-1)
        return _ctx, src_out, _mask

    def forward_decoder(
        self,
        #
        noise_level: torch.Tensor,
        #
        tgt: torch.Tensor,
        tgt_padding_mask: torch.Tensor,
        #
        ctx: Tuple[torch.Tensor, torch.Tensor, torch.Tensor],
    ):
        """
        Args:
            noise_level:      shape (B)
            tgt:              shape (B, T2, ?)
            tgt_padding_mask: shape (B, T2)
            ctx:          shape (B, ?)
        """
        _ctx, mem, mem_padding_mask = ctx
        _ctx = self.c_pos_enc(_ctx, noise_level)

        _tgt = self.dec_in_proj(tgt)

        cls_out, tgt_out = None, None
        if self.use_x_atten:
            cls_out, tgt_out = self.dec(
                _tgt,
                mem,
                padding_mask=tgt_padding_mask,
                mem_padding_mask=mem_padding_mask,
                condition=_ctx,
            )
        else:
            cls_out, tgt_out = self.dec(
                _tgt,
                padding_mask=tgt_padding_mask,
                condition=_ctx,
            )

        # (B, T, ?)
        _tgt_out = self.out_proj(tgt_out)
        return _tgt_out

    def forward(
        self,
        #
        intent_dict: Dict[str, torch.Tensor],
        intent_mask: torch.Tensor,
        #
        other: torch.Tensor,
        other_mask: torch.Tensor,
        #
        src: torch.Tensor,
        src_padding_mask: torch.Tensor,
        #
        noise_level: torch.Tensor,
        #
        tgt: torch.Tensor,
        tgt_padding_mask: torch.Tensor,
    ):
        src_args = (
            intent_dict,
            intent_mask,
            other,
            other_mask,
            src,
            src_padding_mask,
        )
        ctx = self.forward_encoder(*src_args)

        tgt_args = (tgt, tgt_padding_mask, ctx)
        _tgt = self.forward_decoder(noise_level, *tgt_args)
        return _tgt
