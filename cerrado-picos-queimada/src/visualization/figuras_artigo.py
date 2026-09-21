"""Gera todas as figuras e tabelas citadas no artigo.

Executar: python -m src.visualization.figuras_artigo
Cada função devolve o caminho do arquivo salvo em results/figures/, para que a
correspondência figura <-> código fique explícita no artigo (REFORMS 2e).
"""
from __future__ import annotations

from src.config import FIGURAS


def main() -> None:
    FIGURAS.mkdir(parents=True, exist_ok=True)
    # fig01_sazonalidade_mensal
    # fig02_variacao_interanual
    # fig03_heatmap_mes_ano
    # fig04_mapa_densidade_focos
    # fig05_correlacao_anomalias
    # fig06_distribuicao_alvo
    # fig07_curva_precisao_revocacao
    # fig08_importancia_variaveis
    raise NotImplementedError


if __name__ == "__main__":
    main()
