"""Gera defasagens, climatologia e variável-alvo; grava o painel modelável.

Executar: python -m src.features.build_features
Saída: data/processed/painel_features.parquet
"""
from __future__ import annotations

from src.config import carregar_params, fixar_seed


def main() -> None:
    fixar_seed()
    params = carregar_params()
    # 1. marcar split temporal (treino/validacao/teste)
    # 2. estimar climatologia e limiar SOMENTE no treino
    # 3. aplicar alvo ao painel inteiro
    # 4. adicionar defasagens e janelas climáticas
    # 5. salvar painel_features.parquet + tabela descritiva em results/tables/
    raise NotImplementedError


if __name__ == "__main__":
    main()
