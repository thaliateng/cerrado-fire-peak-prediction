"""Download das séries meteorológicas do INMET (BDMEP) para data/raw/.

Executar: python -m src.data.download_inmet

Se o portal exigir preenchimento manual de formulário, documentar aqui o
procedimento passo a passo e versionar apenas o manifesto dos arquivos obtidos
(REFORMS 2d, 2e).
"""
from __future__ import annotations

from src.config import DADOS_BRUTOS, carregar_params


def baixar_estacao(codigo: str, inicio: str, fim: str) -> None:
    raise NotImplementedError


def main() -> None:
    p = carregar_params()
    DADOS_BRUTOS.mkdir(parents=True, exist_ok=True)
    for codigo in p["clima"]["estacoes"]:
        baixar_estacao(codigo, p["periodo"]["inicio"], p["periodo"]["fim"])


if __name__ == "__main__":
    main()
