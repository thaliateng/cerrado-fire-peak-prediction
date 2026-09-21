# Dicionário de dados

## 1. Focos de calor — INPE / BDQueimadas

Arquivos anuais do satélite de referência, formato CSV.
Fonte: Programa Queimadas, INPE. Acesso livre.
Período utilizado: 01/01/2015 a 31/12/2024. Registros no Cerrado: 619.625.

| Campo | Tipo | Descrição | Observação |
|---|---|---|---|
| `id` | texto | Identificador do foco | Usado para checar duplicidades |
| `data_hora_gmt` | datetime | Momento da passagem do satélite | GMT |
| `latitude` | float | Latitude do foco | graus decimais |
| `longitude` | float | Longitude do foco | graus decimais |
| `estado` | texto | UF | |
| `municipio` | texto | Município | |
| `bioma` | texto | Bioma | Filtro = Cerrado |

Derivadas: `celula_id`, `ano`, `mes`, `focos_mes` (contagem por célula × mês).

## 2. Clima — INMET / BDMEP

Séries das estações listadas em `config/params.yaml`.

| Campo | Tipo | Descrição | Observação |
|---|---|---|---|
| `data` | date | Data da medição | |
| `estacao` | texto | Código da estação | |
| `precipitacao_mm` | float | Chuva no dia | registrada em horário fixo |
| `temp_max_c` | float | Temperatura máxima | |
| `temp_min_c` | float | Temperatura mínima | |
| `umidade_rel_pct` | float | Umidade relativa | |
| `insolacao_h` | float | Insolação | |

**Nota importante sobre ausentes:** em torno de 67% das linhas horárias não
trazem temperatura máxima/mínima, chuva e insolação. Isso é estrutural — cada
variável diária é registrada em um único horário (0000 ou 1200 UTC) — e não
falha de coleta. A agregação mensal resolve o caso (ver `docs/decisoes.md`).

## 3. Painel analítico (`data/processed/painel.parquet`)

Uma linha por célula × mês.

| Campo | Tipo | Descrição |
|---|---|---|
| `celula_id` | texto | Identificador da célula de grade |
| `lat_centro`, `lon_centro` | float | Centro da célula |
| `ano_mes` | period | Mês de referência |
| `focos` | int | Focos observados na célula no mês |
| `climatologia_mes` | float | Média de focos da célula naquele mês-calendário (**só treino**) |
| `razao` | float | `focos / climatologia_mes` |
| `pico` | int | Variável-alvo: 1 se `razao` > limiar e `focos` >= mínimo absoluto |
| `chuva_acum_*`, `umidade_media_*`, `temp_media_*` | float | Agregados climáticos defasados |
| `focos_lag_*` | float | Focos defasados |
| `split` | texto | treino / validacao / teste |

## 4. Dados externos (`data/external/`)

| Arquivo | Descrição | Fonte |
|---|---|---|
| `bioma_cerrado.geojson` | Polígono oficial do bioma | IBGE |
| `oni.csv` | Índice ONI (El Niño / La Niña), opcional | NOAA |
