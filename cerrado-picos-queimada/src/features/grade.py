"""Atribuição de cada foco a uma célula de grade regular."""
from __future__ import annotations

import numpy as np
import pandas as pd


def atribuir_celula(df: pd.DataFrame, tamanho_graus: float,
                    col_lat: str = "latitude",
                    col_lon: str = "longitude") -> pd.DataFrame:
    """Adiciona `celula_id`, `lat_centro` e `lon_centro`.

    A célula é definida pelo canto inferior esquerdo arredondado para baixo no
    múltiplo de `tamanho_graus`, o que torna a atribuição determinística e
    reproduzível.
    """
    lat0 = np.floor(df[col_lat] / tamanho_graus) * tamanho_graus
    lon0 = np.floor(df[col_lon] / tamanho_graus) * tamanho_graus
    meio = tamanho_graus / 2
    out = df.copy()
    out["lat_centro"] = lat0 + meio
    out["lon_centro"] = lon0 + meio
    out["celula_id"] = (
        out["lat_centro"].round(3).astype(str) + "_" + out["lon_centro"].round(3).astype(str)
    )
    return out
