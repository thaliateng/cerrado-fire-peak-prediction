"""Carregamento centralizado dos parâmetros do estudo.

Nenhum módulo deve conter números mágicos: tudo vem de config/params.yaml.
"""
from __future__ import annotations

import random
from pathlib import Path

import numpy as np
import yaml

RAIZ = Path(__file__).resolve().parents[1]
DADOS_BRUTOS = RAIZ / "data" / "raw"
DADOS_INTERIM = RAIZ / "data" / "interim"
DADOS_PROCESSADOS = RAIZ / "data" / "processed"
DADOS_EXTERNOS = RAIZ / "data" / "external"
RESULTADOS = RAIZ / "results"
FIGURAS = RESULTADOS / "figures"
TABELAS = RESULTADOS / "tables"
MODELOS = RESULTADOS / "models"


def carregar_params(caminho: Path | None = None) -> dict:
    caminho = caminho or RAIZ / "config" / "params.yaml"
    with open(caminho, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def fixar_seed(seed: int | None = None) -> int:
    """Fixa a semente global (REFORMS 2e)."""
    seed = seed if seed is not None else carregar_params()["projeto"]["seed"]
    random.seed(seed)
    np.random.seed(seed)
    return seed
