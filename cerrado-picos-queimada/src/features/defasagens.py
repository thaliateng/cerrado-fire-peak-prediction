"""Features defasadas: só informação disponível até o fim do mês t (REFORMS 6c)."""
from __future__ import annotations

import pandas as pd


def adicionar_defasagens_focos(painel: pd.DataFrame, lags: list[int]) -> pd.DataFrame:
    out = painel.sort_values(["celula_id", "ano_mes"]).copy()
    for lag in lags:
        out[f"focos_lag_{lag}"] = out.groupby("celula_id")["focos"].shift(lag)
    return out


def adicionar_janelas_climaticas(painel: pd.DataFrame, coluna: str,
                                 janelas: list[int], prefixo: str) -> pd.DataFrame:
    """Acumulados/médias das janelas anteriores, sempre com `shift(1)` aplicado
    antes da janela para nunca incluir o mês previsto."""
    out = painel.sort_values(["celula_id", "ano_mes"]).copy()
    base = out.groupby("celula_id")[coluna].shift(1)
    for j in janelas:
        out[f"{prefixo}_{j}m"] = (
            base.groupby(out["celula_id"]).rolling(j, min_periods=j).mean()
            .reset_index(level=0, drop=True)
        )
    return out
