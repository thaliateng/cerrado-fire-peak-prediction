"""Agregação mensal do clima e associação célula -> estação mais próxima."""
from __future__ import annotations

import numpy as np
import pandas as pd

RAIO_TERRA_KM = 6371.0


def distancia_haversine_km(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, (lat1, lon1, lat2, lon2))
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    return 2 * RAIO_TERRA_KM * np.arcsin(np.sqrt(a))


def associar_estacao(celulas: pd.DataFrame, estacoes: pd.DataFrame,
                     raio_max_km: float) -> pd.DataFrame:
    """Associa cada célula à estação INMET mais próxima dentro do raio máximo.

    Células sem estação dentro do raio são marcadas com `estacao = NaN` e devem
    ser excluídas do painel, com a exclusão registrada (REFORMS 4a).
    """
    raise NotImplementedError


def agregar_mensal(clima_diario: pd.DataFrame) -> pd.DataFrame:
    """Agrega o diário em mensal usando apenas registros válidos por variável.

    Os ausentes do INMET são estruturais (cada variável é registrada em um
    horário fixo), não falha de coleta — ver docs/decisoes.md D05. Retorna
    também a cobertura (nº de dias válidos) de cada variável no mês, para que a
    qualidade da agregação possa ser reportada.
    """
    raise NotImplementedError
