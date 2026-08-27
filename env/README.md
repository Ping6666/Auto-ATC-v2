# Env

## conda

```bash=
conda env create -f ./env/environment.yml

conda env list
conda env remove -n auto-atc-v2
```

## uv

```bash=
conda activate auto-atc-v2

uv pip install -r ./env/requirements.txt
```
