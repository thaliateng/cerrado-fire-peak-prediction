"""Download dos arquivos anuais de focos do BDQueimadas (INPE) para data/raw/.

Executar: python -m src.data.download_inpe
"""
from __future__ import annotations

from src.config import DADOS_BRUTOS, carregar_params


def baixar_focos(ano_inicio: int, ano_fim: int) -> None:
    """Baixa os CSV anuais do satélite de referência.

    TODO: preencher a URL base do portal do INPE e iterar por ano, salvando em
    DADOS_BRUTOS / f"focos_br_ref_{ano}.csv". Registrar a data de acesso em
    data/raw/MANIFEST.md (REFORMS 3a).
    """
    raise NotImplementedError


def main() -> None:
    p = carregar_params()
    DADOS_BRUTOS.mkdir(parents=True, exist_ok=True)
    inicio = int(p["periodo"]["inicio"][:4])
    fim = int(p["periodo"]["fim"][:4])
    baixar_focos(inicio, fim)


if __name__ == "__main__":
    main()
