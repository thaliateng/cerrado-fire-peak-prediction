"""Treino dos modelos candidatos com validação temporal.

Executar: python -m src.models.train
Saídas: results/models/*.joblib e results/tables/hiperparametros.csv
"""
from __future__ import annotations

from src.config import MODELOS, carregar_params, fixar_seed


def main() -> None:
    fixar_seed()
    params = carregar_params()
    MODELOS.mkdir(parents=True, exist_ok=True)
    # 1. carregar painel_features.parquet
    # 2. montar Pipeline (imputação + escala + modelo) — ajustado só no treino
    # 3. busca de hiperparâmetros com TimeSeriesSplit ou origem móvel
    # 4. salvar melhor configuração de cada modelo + grade testada (REFORMS 5e)
    raise NotImplementedError


if __name__ == "__main__":
    main()
