"""Monta o painel célula x mês a partir dos dados brutos.

Executar: python -m src.features.build_painel
Saída: data/processed/painel.parquet
"""
from __future__ import annotations

from src.config import DADOS_PROCESSADOS, carregar_params, fixar_seed


def main() -> None:
    fixar_seed()
    params = carregar_params()
    DADOS_PROCESSADOS.mkdir(parents=True, exist_ok=True)
    # 1. carregar focos e filtrar bioma/período
    # 2. atribuir célula de grade (src.features.grade)
    # 3. contar focos por célula x mês
    # 4. agregar clima mensal e associar estação (src.features.clima)
    # 5. juntar e salvar painel.parquet
    raise NotImplementedError


if __name__ == "__main__":
    main()
