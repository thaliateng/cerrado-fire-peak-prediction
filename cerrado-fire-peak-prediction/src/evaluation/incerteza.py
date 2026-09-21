"""Intervalos de confiança por bootstrap em blocos anuais (REFORMS 7b).

Reamostragem simples por linha é inadequada: observações da mesma célula e do
mesmo ano são fortemente correlacionadas.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def bootstrap_blocos(df: pd.DataFrame, funcao_metrica, col_bloco: str = "ano",
                     n: int = 1000, seed: int = 42) -> tuple[float, float, float]:
    """Retorna (estimativa, limite inferior 2,5%, limite superior 97,5%)."""
    rng = np.random.default_rng(seed)
    blocos = df[col_bloco].unique()
    estimativas = []
    for _ in range(n):
        escolhidos = rng.choice(blocos, size=len(blocos), replace=True)
        amostra = pd.concat([df[df[col_bloco] == b] for b in escolhidos])
        estimativas.append(funcao_metrica(amostra))
    return (
        float(funcao_metrica(df)),
        float(np.percentile(estimativas, 2.5)),
        float(np.percentile(estimativas, 97.5)),
    )
