"""Construção da variável-alvo `pico` sem vazamento temporal.

A climatologia por célula e mês-calendário e o limiar do percentil são estimados
SOMENTE no período de treino e depois aplicados a validação e teste
(REFORMS 6a; docs/decisoes.md D04).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def estimar_climatologia(painel_treino: pd.DataFrame) -> pd.DataFrame:
    """Média de focos por célula e mês-calendário no período de treino."""
    return (
        painel_treino.groupby(["celula_id", "mes"], as_index=False)["focos"]
        .mean()
        .rename(columns={"focos": "climatologia_mes"})
    )


def aplicar_alvo(painel: pd.DataFrame, climatologia: pd.DataFrame,
                 limiar_razao: float, min_focos_absoluto: int,
                 meses_considerados: list[int]) -> pd.DataFrame:
    """Anexa `razao` e `pico` ao painel completo."""
    out = painel.merge(climatologia, on=["celula_id", "mes"], how="left")
    out["razao"] = out["focos"] / out["climatologia_mes"].replace(0, np.nan)
    out["pico"] = (
        (out["razao"] > limiar_razao)
        & (out["focos"] >= min_focos_absoluto)
        & (out["mes"].isin(meses_considerados))
    ).astype(int)
    return out


def calcular_limiar(painel_treino_com_razao: pd.DataFrame, percentil: int) -> float:
    """Limiar da razão, estimado apenas no treino."""
    return float(np.nanpercentile(painel_treino_com_razao["razao"], percentil))
