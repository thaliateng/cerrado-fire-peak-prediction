# Predição de picos de queimada no Cerrado

Previsão, com um mês de antecedência, de anomalias positivas de focos de queimada
no bioma Cerrado, usando dados do INPE (BDQueimadas) e do INMET, no período
2015–2024. A unidade de análise é **célula de grade × mês**.

Trabalho final da disciplina *Ferramentas e Fundamentos em Ciência de Dados* —
Mestrado Profissional em Ciência de Dados, UFPR.

---

## 1. Problema e pergunta de pesquisa

A ocorrência de queimadas no Cerrado segue um padrão sazonal forte, com pico em
agosto e setembro. O que causa dano ambiental severo, porém, não é a estação seca
em si, mas os meses em que os focos ficam **acima do padrão histórico daquele mês**.

> **Pergunta:** é possível prever, com um mês de antecedência, quais regiões do
> Cerrado apresentarão número de focos anormalmente alto para a época do ano, a
> partir do clima antecedente e do histórico recente de focos?

- **População / distribuição:** bioma Cerrado, 2015–2024, agregado em células de
  grade regular de 1° × 1° (configurável em `config/params.yaml`).
- **Unidade de análise:** célula de grade × mês.
- **Horizonte de previsão:** com informação disponível até o fim do mês *t*,
  prever a condição do mês *t+1*.
- **Variável-alvo:** binária. `pico = 1` quando a razão entre os focos observados
  na célula no mês e a climatologia daquela célula para aquele mês-calendário
  (estimada **somente com dados de treino**) supera o limiar definido em
  `config/params.yaml`.
- **Métrica principal:** PR-AUC (área sob a curva precisão–revocação), adequada a
  classes desbalanceadas.

## 2. Fontes de dados

| Base | Fonte | Período | Acesso |
|---|---|---|---|
| Focos de calor (satélite de referência) | INPE — Programa Queimadas / BDQueimadas | 2015–2024 | https://terrabrasilis.dpi.inpe.br/queimadas/portal/ |
| Séries meteorológicas (estações convencionais / automáticas) | INMET — Banco de Dados Meteorológicos | 2015–2024 | https://bdmep.inmet.gov.br/ |

Os dados **não são versionados neste repositório** (volume e política de
redistribuição). Use `make data` ou os scripts em `src/data/` para baixá-los.
Detalhes de cada variável em [`docs/dicionario_de_dados.md`](docs/dicionario_de_dados.md).

## 3. Como reproduzir

```bash
# 1. clonar
git clone https://github.com/<usuario>/cerrado-picos-queimada.git
cd cerrado-picos-queimada

# 2. ambiente (Python 3.11)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. pipeline completo (download -> painel -> features -> modelos -> avaliação)
make all
```

Alternativa sem `make`:

```bash
bash run_all.sh
```

Cada etapa isolada:

```bash
make data        # baixa INPE e INMET para data/raw/
make painel      # monta o painel célula × mês em data/processed/
make features    # gera defasagens e variável-alvo
make train       # treina baselines e modelos
make evaluate    # métricas, intervalos e figuras em results/
```

Tempo aproximado de execução e ambiente computacional usado: ver
[`docs/ambiente.md`](docs/ambiente.md).

## 4. Estrutura do repositório

```
.
├── config/params.yaml        # todos os parâmetros do estudo (grade, limiar, splits, seeds)
├── data/
│   ├── raw/                  # dados brutos baixados (não versionado)
│   ├── interim/              # intermediários (não versionado)
│   ├── processed/            # painel final usado pelos modelos (não versionado)
│   └── external/             # dados auxiliares (ex.: shapefile do bioma, índice ONI)
├── notebooks/                # exploração e narrativa, na ordem 01..06
├── src/
│   ├── data/                 # download e carga
│   ├── features/             # grade, junção climática, defasagens, alvo
│   ├── models/               # baselines, treino, ajuste de hiperparâmetros
│   ├── evaluation/           # métricas, incerteza, análise de erro
│   └── visualization/        # figuras do artigo
├── results/
│   ├── figures/              # figuras exportadas (versionadas)
│   ├── tables/               # tabelas em CSV/Markdown (versionadas)
│   └── models/               # modelos serializados (não versionado)
├── docs/
│   ├── artigo/               # manuscrito e referências
│   ├── reforms_checklist.md  # checklist REFORMS preenchido
│   ├── dicionario_de_dados.md
│   ├── decisoes.md           # registro de decisões metodológicas
│   └── ambiente.md           # infraestrutura computacional
└── tests/                    # testes das funções críticas (alvo, defasagens, splits)
```

## 5. Decisões metodológicas que protegem contra vazamento

1. A climatologia por célula e mês-calendário e o limiar de pico são estimados
   **apenas no período de treino** e aplicados aos períodos de validação e teste.
2. Todas as variáveis preditoras usam apenas informação disponível até o fim do
   mês *t*. Nenhuma variável do mês previsto entra no modelo.
3. A divisão é **temporal**, nunca aleatória: treino 2015–2021, validação 2022,
   teste 2023–2024 (ver `config/params.yaml`).
4. Normalização e imputação vivem dentro de um `Pipeline` do scikit-learn,
   ajustado somente no treino.
5. Células vizinhas no mesmo mês são correlacionadas; a validação por blocos
   espaciais está descrita em `docs/decisoes.md`.

## 6. Modelos e avaliação

**Baselines:** climatologia (prever sempre a classe majoritária) e persistência
(se o mês anterior foi anômalo, prever anômalo).

**Modelos:** regressão logística regularizada, Random Forest e gradient boosting
(LightGBM ou XGBoost).

**Métricas:** PR-AUC (principal), revocação e precisão da classe pico, F1 e
Brier score. Acurácia não é reportada como métrica de seleção por causa do
desbalanceamento. Intervalos de confiança por bootstrap em blocos anuais.

## 7. Conformidade com o REFORMS

O estudo é documentado segundo o checklist
[REFORMS](https://reforms.cs.princeton.edu) (Kapoor et al., 2024). O mapeamento
item a item está em [`docs/reforms_checklist.md`](docs/reforms_checklist.md).

## 8. Licença

Código sob licença MIT (ver `LICENSE`). Textos e figuras sob CC BY 4.0. Os dados
originais pertencem ao INPE e ao INMET e estão sujeitos às respectivas políticas
de uso.

## 9. Como citar

Ver `CITATION.cff`.
