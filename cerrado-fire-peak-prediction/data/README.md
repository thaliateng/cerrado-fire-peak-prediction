# Dados

Esta pasta **não versiona dados**, apenas a estrutura. Rode `make data` para
baixar tudo, ou siga as instruções abaixo se o download automático falhar.

- `raw/` — arquivos exatamente como baixados do INPE e do INMET. Nunca editar.
- `interim/` — intermediários (focos por célula, clima mensal).
- `processed/` — `painel.parquet` e `painel_features.parquet`, usados pelos modelos.
- `external/` — polígono do bioma (IBGE) e, se usado, índice ONI (NOAA).

Ao baixar manualmente, registre em `raw/MANIFEST.md`: nome do arquivo, URL exata,
data de acesso e tamanho. Isso atende ao item 3a do REFORMS.
