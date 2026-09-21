"""Leitura dos dados brutos com tipos e nomes de coluna padronizados."""
from __future__ import annotations

import pandas as pd

from src.config import DADOS_BRUTOS


def carregar_focos() -> pd.DataFrame:
    """Concatena os CSV anuais do INPE e padroniza colunas."""
    arquivos = sorted(DADOS_BRUTOS.glob("focos_br_ref_*.csv"))
    if not arquivos:
        raise FileNotFoundError("Rode `make data` antes.")
    df = pd.concat((pd.read_csv(a) for a in arquivos), ignore_index=True)
    return df


def carregar_clima() -> pd.DataFrame:
    """Concatena as séries das estações INMET e padroniza colunas."""
    arquivos = sorted(DADOS_BRUTOS.glob("inmet_*.csv"))
    if not arquivos:
        raise FileNotFoundError("Rode `make data` antes.")
    return pd.concat((pd.read_csv(a) for a in arquivos), ignore_index=True)
