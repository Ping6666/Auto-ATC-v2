from typing import Dict, Optional
import math

import torch

from core.utils import get_tensor_like


def modulate(x: torch.Tensor, shift: torch.Tensor, scale: torch.Tensor):
    return x * (1. + scale) + shift


# --- #


class DiscretePositionalEncoding(torch.nn.Module):

    pe: torch.Tensor

    def __init__(
        self,
        d_model: int,
        dropout: float,
        max_len: int = 100,
        magic_num: float = 10000.0,
    ):
        super().__init__()
        assert d_model % 2 == 0

        # pos.shape = (S, 1)
        pos = torch.arange(0, max_len).float().unsqueeze(-1)

        # div_term.shape = (D)
        _dt = torch.arange(0, d_model, 2).float()
        div_term = torch.exp(_dt * -(math.log(magic_num) / d_model))

        pe = torch.zeros(max_len, d_model)
        pe[..., 0::2] = torch.sin(pos * div_term)
        pe[..., 1::2] = torch.cos(pos * div_term)

        # pe.shape = (S, D)
        self.register_buffer("pe", pe)

        #

        self.max_len = max_len

        self.sequential = torch.nn.Sequential(
            torch.nn.Linear(d_model, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, d_model),
        )
        self.dropout = torch.nn.Dropout(p=dropout)
        return

    def forward(self, x: torch.Tensor):
        _len = x.shape[-2]
        if _len > self.max_len:
            print(f"{x.shape = }")
            print(f"{_len = } {self.max_len = }")
            raise AssertionError

        _pe = self.pe[:_len].requires_grad_(False)
        _pe = get_tensor_like(_pe, x, dim=0)

        x = x + self.sequential(_pe)
        return self.dropout(x)


class ContinuousPositionalEncoding(torch.nn.Module):

    div_term: torch.Tensor

    def __init__(
        self,
        d_model: int,
        dropout: float,
        n_features: int,
        magic_num: float = 10000.0,
    ):
        super().__init__()
        assert d_model % 2 == 0

        half_d_model = d_model // 2
        self.d_model = d_model

        # div_term.shape = (D // 2)
        _dt = torch.arange(half_d_model).float()
        div_term = torch.exp(_dt * -(math.log(magic_num) / half_d_model))

        self.register_buffer('div_term', div_term)

        #

        self.sequential = torch.nn.Sequential(
            torch.nn.Linear(d_model, d_model),
            torch.nn.SiLU(),
            torch.nn.Linear(d_model, n_features),
        )
        self.dropout = torch.nn.Dropout(p=dropout)
        return

    def forward(self, x: torch.Tensor, t: torch.Tensor):
        _t = get_tensor_like(t, x)
        _div_term = get_tensor_like(self.div_term, x, dim=0)
        _pe = _t * _div_term

        _size = (*_pe.shape[:-1], self.d_model)
        pe = torch.zeros(*_size).to(x.device)
        pe[..., 0::2] = torch.sin(_pe)
        pe[..., 1::2] = torch.cos(_pe)

        # TODO
        x = x + self.sequential(pe)
        return self.dropout(x)


# --- #


class MultiheadAttention(torch.nn.Module):

    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        dropout: float = 0,
        bias: bool = True,
    ):
        super().__init__()

        assert embed_dim % num_heads == 0

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.scaling = math.pow(self.head_dim, -0.5)

        #

        self.q_proj = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.k_proj = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.v_proj = torch.nn.Linear(embed_dim, embed_dim, bias=bias)
        self.out_proj = torch.nn.Linear(embed_dim, embed_dim, bias=bias)

        self.dropout = torch.nn.Dropout(p=dropout)
        return

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        attn_bias: Optional[torch.Tensor] = None,
        key_padding_mask: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        # ref.: https://github.com/microsoft/Graphormer/blob/main/graphormer/modules/multihead_attention.py#L99

        _tgt_shape = query.shape
        bs, tgt_len, _ = _tgt_shape
        _, src_len, _ = key.shape

        q: torch.Tensor = self.q_proj(query)
        k: torch.Tensor = self.k_proj(key)
        v: torch.Tensor = self.v_proj(value)

        q *= self.scaling

        _size = (bs, -1, self.num_heads, self.head_dim)
        _size_tgt1 = (bs * self.num_heads, tgt_len, self.head_dim)
        _size_tgt2 = (bs, self.num_heads, tgt_len, self.head_dim)
        _size_src = (bs * self.num_heads, src_len, self.head_dim)
        _size1 = (bs * self.num_heads, tgt_len, src_len)
        _size2 = (bs, self.num_heads, tgt_len, src_len)

        q = q.reshape(*_size).transpose(1, 2).reshape(*_size_tgt1)
        k = k.reshape(*_size).transpose(1, 2).reshape(*_size_src)
        v = v.reshape(*_size).transpose(1, 2).reshape(*_size_src)

        # attn_weights.shape: _size1
        attn_weights = torch.bmm(q, k.transpose(-2, -1))

        if attn_bias is not None:
            attn_weights += attn_bias.reshape(*_size1)

        if attn_mask is not None:
            # attn_mask must have shape (tgt_len, src_len) or _size1
            attn_weights += get_tensor_like(attn_mask, attn_weights)

        if key_padding_mask is not None:
            attn_weights = attn_weights.reshape(*_size2)
            _mask = get_tensor_like(key_padding_mask, attn_weights, dim=1)
            attn_weights = attn_weights.masked_fill(_mask, float("-inf"))
            attn_weights = attn_weights.reshape(*_size1)

        attn_weights = attn_weights.softmax(dim=-1).type_as(attn_weights)
        attn_probs = self.dropout(attn_weights)

        # attn.shape: _size_tgt1
        attn = torch.bmm(attn_probs, v)

        attn = attn.reshape(_size_tgt2).transpose(1, 2).reshape(_tgt_shape)
        attn = self.out_proj(attn)
        return attn


class AdaLN(torch.nn.Module):

    def __init__(
        self,
        n_features: int,
        #
        num_chunks: int,
        d_model: int,
    ):
        super().__init__()

        self.num_chunks = num_chunks
        self.d_model = d_model
        out_features = self.num_chunks * self.d_model

        self.adaLN_seq = torch.nn.Sequential(
            torch.nn.Linear(n_features, out_features),
            torch.nn.SiLU(),
            torch.nn.Linear(out_features, out_features),
        )
        return

    def forward(self, x: torch.Tensor):
        """
        Args:
            x: with shape (B, F)
        """
        bs, *_ = x.shape
        x = self.adaLN_seq(x)
        # (B, 1, num_chunks * D), broadcast over the sequence dimension.
        return x.reshape(bs, 1, self.num_chunks * self.d_model)


# --- #


class EncoderLayer(torch.nn.Module):

    def __init__(
        self,
        d_model: int,
        nhead: int,
        dim_feedforward: int,
        activation_fn: torch.nn.Module,
        dropout: float,
        #
        adaln_kwargs: Optional[Dict] = None,
    ):
        super().__init__()

        self.sa = MultiheadAttention(d_model, nhead, dropout)
        self.ff = torch.nn.Sequential(
            torch.nn.Linear(d_model, dim_feedforward),
            activation_fn,
            torch.nn.Linear(dim_feedforward, d_model),
        )

        self.sa_norm = torch.nn.LayerNorm(d_model)
        self.ff_norm = torch.nn.LayerNorm(d_model)

        self.sa_dropout = torch.nn.Dropout(dropout)
        self.ff_dropout = torch.nn.Dropout(dropout)

        self.adaLN_seq = None
        if adaln_kwargs is not None:
            self.adaLN_seq = AdaLN(
                **adaln_kwargs,
                d_model=d_model,
                num_chunks=6,
            )
        return

    # self attention block
    def _sa_block(
        self,
        src: torch.Tensor,
        attn_bias: Optional[torch.Tensor] = None,
        src_padding_mask: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Args:
            src: with shape (B, T, D)
            src_padding_mask: with shape (B, T)
        """
        x = self.sa(
            src,
            src,
            src,
            attn_bias=attn_bias,
            key_padding_mask=src_padding_mask,
            attn_mask=attn_mask,
        )
        return self.sa_dropout(x)

    # feedforward block
    def _ff_block(self, x: torch.Tensor) -> torch.Tensor:
        x = self.ff(x)
        return self.ff_dropout(x)

    def forward(
        self,
        src: torch.Tensor,
        attn_bias: Optional[torch.Tensor] = None,
        src_padding_mask: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
        #
        condition: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        kwargs = dict(
            attn_bias=attn_bias,
            src_padding_mask=src_padding_mask,
            attn_mask=attn_mask,
        )

        x = src
        if self.adaLN_seq is None:
            x = x + self._sa_block(self.sa_norm(x), **kwargs)
            x = x + self._ff_block(self.ff_norm(x))
        else:
            assert condition is not None
            _cond = torch.chunk(self.adaLN_seq(condition), chunks=6, dim=-1)
            shift_sa, scale_sa, gate_sa, shift_ff, scale_ff, gate_ff = _cond
            _x = modulate(self.sa_norm(x), shift_sa, scale_sa)
            x = x + gate_sa * self._sa_block(_x, **kwargs)
            _x = modulate(self.ff_norm(x), shift_ff, scale_ff)
            x = x + gate_ff * self._ff_block(_x)
        return x


class DecoderLayer(torch.nn.Module):

    def __init__(
        self,
        d_model: int,
        nhead: int,
        dim_feedforward: int,
        activation_fn: torch.nn.Module,
        dropout: float,
        #
        adaln_kwargs: Optional[Dict] = None,
    ):
        super().__init__()

        self.sa = MultiheadAttention(d_model, nhead, dropout)
        self.ca = MultiheadAttention(d_model, nhead, dropout)
        self.ff = torch.nn.Sequential(
            torch.nn.Linear(d_model, dim_feedforward),
            activation_fn,
            torch.nn.Linear(dim_feedforward, d_model),
        )

        self.sa_norm = torch.nn.LayerNorm(d_model)
        self.ca_norm = torch.nn.LayerNorm(d_model)
        self.ff_norm = torch.nn.LayerNorm(d_model)

        self.sa_dropout = torch.nn.Dropout(dropout)
        self.ca_dropout = torch.nn.Dropout(dropout)
        self.ff_dropout = torch.nn.Dropout(dropout)

        self.adaLN_seq = None
        if adaln_kwargs is not None:
            self.adaLN_seq = AdaLN(
                **adaln_kwargs,
                d_model=d_model,
                num_chunks=9,
            )
        return

    # self attention block
    def _sa_block(
        self,
        tgt: torch.Tensor,
        attn_bias: Optional[torch.Tensor] = None,
        tgt_padding_mask: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Args:
            tgt: with shape (B, T, D)
            tgt_padding_mask: with shape (B, T)
        """
        x = self.sa(
            tgt,
            tgt,
            tgt,
            attn_bias=attn_bias,
            key_padding_mask=tgt_padding_mask,
            attn_mask=attn_mask,
        )
        return self.sa_dropout(x)

    # cross attention block
    def _ca_block(
        self,
        tgt: torch.Tensor,
        mem: torch.Tensor,
        attn_bias: Optional[torch.Tensor] = None,
        mem_padding_mask: Optional[torch.Tensor] = None,
        attn_mask: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Args:
            tgt: with shape (B, T, D)
        """
        x = self.ca(
            tgt,
            mem,
            mem,
            attn_bias=attn_bias,
            key_padding_mask=mem_padding_mask,
            attn_mask=attn_mask,
        )
        return self.ca_dropout(x)

    # feedforward block
    def _ff_block(self, x: torch.Tensor) -> torch.Tensor:
        x = self.ff(x)
        return self.ff_dropout(x)

    def forward(
        self,
        tgt: torch.Tensor,
        mem: torch.Tensor,
        #
        tgt_attn_bias: Optional[torch.Tensor] = None,
        tgt_padding_mask: Optional[torch.Tensor] = None,
        tgt_attn_mask: Optional[torch.Tensor] = None,
        #
        mem_padding_mask: Optional[torch.Tensor] = None,
        mem_attn_mask: Optional[torch.Tensor] = None,
        #
        condition: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        kwargs1 = dict(
            attn_bias=tgt_attn_bias,
            tgt_padding_mask=tgt_padding_mask,
            attn_mask=tgt_attn_mask,
        )
        kwargs2 = dict(
            mem=mem,
            mem_padding_mask=mem_padding_mask,
            attn_mask=mem_attn_mask,
        )

        x = tgt
        if self.adaLN_seq is None:
            x = x + self._sa_block(self.sa_norm(x), **kwargs1)
            x = x + self._ca_block(self.ca_norm(x), **kwargs2)
            x = x + self._ff_block(self.ff_norm(x))
        else:
            assert condition is not None
            _cond = torch.chunk(self.adaLN_seq(condition), chunks=9, dim=-1)
            shift_sa, scale_sa, gate_sa, shift_ca, scale_ca, gate_ca, shift_ff, scale_ff, gate_ff = _cond
            _x = modulate(self.sa_norm(x), shift_sa, scale_sa)
            x = x + gate_sa * self._sa_block(_x, **kwargs1)
            _x = modulate(self.ca_norm(x), shift_ca, scale_ca)
            x = x + gate_ca * self._ca_block(_x, **kwargs2)
            _x = modulate(self.ff_norm(x), shift_ff, scale_ff)
            x = x + gate_ff * self._ff_block(_x)
        return x


# --- #


class TrajEncBlock(torch.nn.Module):

    def __init__(
        self,
        #
        seq_len: int,
        #
        d_model: int,
        nhead: int,
        widening_factor: int,
        num_layers: int,
        dropout: float = 0.,
        #
        cond_n_features: Optional[int] = None,
    ):
        super().__init__()

        _seq_len = seq_len + 1  # one for extra pad
        ff_dim = d_model * widening_factor

        adaln_kwargs = None
        if cond_n_features is not None:
            adaln_kwargs = dict(
                n_features=cond_n_features,
            )

        #

        self.extra_pad = torch.nn.Parameter(torch.randn(1, d_model))
        self.pos_enc = DiscretePositionalEncoding(
            d_model,
            dropout,
            max_len=_seq_len,
        )

        self.blocks = torch.nn.ModuleList([
            EncoderLayer(
                d_model,
                nhead,
                ff_dim,
                torch.nn.GELU(approximate='tanh'),
                dropout,
                adaln_kwargs=adaln_kwargs,
            ) for _ in range(num_layers)
        ])
        self.norm = torch.nn.LayerNorm(d_model)
        return

    def forward(
        self,
        x: torch.Tensor,
        padding_mask: Optional[torch.Tensor] = None,
        condition: Optional[torch.Tensor] = None,
    ):
        """
        Args:
            x: with shape (B, T, D)
        """

        # (B, T, D) => (B, 1 + T, D)
        _pad = self.extra_pad.unsqueeze(0).expand(len(x), -1, -1)
        x = torch.cat((_pad, x), dim=1)

        if padding_mask is not None:
            # (B, T) => (B, 1 + T)
            padding_mask = torch.nn.functional.pad(
                padding_mask,
                # pad the last dim with (l, r) = (1, 0)
                pad=(1, 0),
                mode='constant',
                value=False,
            )

        x = self.pos_enc(x)
        for block in self.blocks:
            x = block(x, src_padding_mask=padding_mask, condition=condition)
        x = self.norm(x)
        return x[:, 0, :], x[:, 1:, :]


class TrajDecBlock(torch.nn.Module):

    def __init__(
        self,
        #
        seq_len: int,
        #
        d_model: int,
        nhead: int,
        widening_factor: int,
        num_layers: int,
        dropout: float = 0.,
        #
        cond_n_features: Optional[int] = None,
    ):
        super().__init__()

        _seq_len = seq_len + 1  # one for extra pad
        ff_dim = d_model * widening_factor

        adaln_kwargs = None
        if cond_n_features is not None:
            adaln_kwargs = dict(
                n_features=cond_n_features,
            )

        #

        self.extra_pad = torch.nn.Parameter(torch.randn(1, d_model))
        self.mem_extra_pad = torch.nn.Parameter(torch.randn(1, d_model))
        self.pos_enc = DiscretePositionalEncoding(
            d_model,
            dropout,
            max_len=_seq_len,
        )

        self.blocks = torch.nn.ModuleList([
            DecoderLayer(
                d_model,
                nhead,
                ff_dim,
                torch.nn.GELU(approximate='tanh'),
                dropout,
                adaln_kwargs=adaln_kwargs,
            ) for _ in range(num_layers)
        ])
        self.norm = torch.nn.LayerNorm(d_model)
        return

    def forward(
        self,
        x: torch.Tensor,
        mem: torch.Tensor,
        padding_mask: Optional[torch.Tensor] = None,
        mem_padding_mask: Optional[torch.Tensor] = None,
        condition: Optional[torch.Tensor] = None,
    ):
        """
        Args:
            x: with shape (B, T, D)
        """

        # (B, T, D) => (B, 1 + T, D)
        _pad = self.extra_pad.unsqueeze(0).expand(len(x), -1, -1)
        x = torch.cat((_pad, x), dim=1)

        if padding_mask is not None:
            # (B, T) => (B, 1 + T)
            padding_mask = torch.nn.functional.pad(
                padding_mask,
                # pad the last dim with (l, r) = (1, 0)
                pad=(1, 0),
                mode='constant',
                value=False,
            )

        # (B, T, D) => (B, 1 + T, D)
        _mem_pad = self.mem_extra_pad.unsqueeze(0).expand(len(mem), -1, -1)
        mem = torch.cat((_mem_pad, mem), dim=1)

        if mem_padding_mask is not None:
            # (B, T) => (B, 1 + T)
            mem_padding_mask = torch.nn.functional.pad(
                mem_padding_mask,
                # pad the last dim with (l, r) = (1, 0)
                pad=(1, 0),
                mode='constant',
                value=False,
            )

        x = self.pos_enc(x)
        for block in self.blocks:
            x = block(
                x,
                mem,
                tgt_padding_mask=padding_mask,
                mem_padding_mask=mem_padding_mask,
                condition=condition,
            )
        x = self.norm(x)
        return x[:, 0, :], x[:, 1:, :]


# --- #


class TrajGen(torch.nn.Module):

    def __init__(self):
        super().__init__()
        return

    def forward_encoder(self):
        raise NotImplementedError

    def forward_decoder(self):
        raise NotImplementedError

    def forward(self):
        raise NotImplementedError
