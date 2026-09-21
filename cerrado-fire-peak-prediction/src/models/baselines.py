"""Baselines obrigatórios para comparação (REFORMS 5f)."""
from __future__ import annotations

import numpy as np
import pandas as pd


def baseline_classe_majoritaria(y_treino: pd.Series, n_teste: int) -> np.ndarray:
    """Prevê sempre a classe mais frequente do treino."""
    classe = int(y_treino.mode().iloc[0])
    return np.full(n_teste, classe)


def baseline_persistencia(painel_teste: pd.DataFrame) -> np.ndarray:
    """Prevê pico se a célula foi pico no mês anterior."""
    return painel_teste["pico_lag_1"].fillna(0).to_numpy().astype(int)


def baseline_climatologia(painel_teste: pd.DataFrame) -> np.ndarray:
    """Probabilidade histórica de pico da célula naquele mês-calendário."""
    return painel_teste["prob_hist_pico"].fillna(0).to_numpy()
