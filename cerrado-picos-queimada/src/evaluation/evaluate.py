"""Avaliação final no conjunto de teste e análise de erro.

Executar: python -m src.evaluation.evaluate
Saídas: results/tables/desempenho.csv, results/figures/*.png
"""
from __future__ import annotations

from src.config import TABELAS, carregar_params, fixar_seed


def main() -> None:
    fixar_seed()
    params = carregar_params()
    TABELAS.mkdir(parents=True, exist_ok=True)
    # 1. carregar modelos e painel de teste
    # 2. métricas + bootstrap em blocos para cada modelo e baseline
    # 3. curva precisão-revocação e matriz de confusão
    # 4. análise de erro: quais picos foram perdidos (ano, célula, mês)
    # 5. importância das variáveis (permutação / SHAP)
    raise NotImplementedError


if __name__ == "__main__":
    main()
