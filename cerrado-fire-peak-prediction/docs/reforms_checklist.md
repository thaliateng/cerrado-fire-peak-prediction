# Checklist REFORMS — aplicado ao estudo

Legenda: ✓ atendido · △ parcialmente atendido · ✗ não atendido · N/A não se aplica

Preencher a coluna "Onde está / o que falta" apontando seção, tabela, figura ou
arquivo. Este arquivo espelha o documento ATIVIDADE FINAL da disciplina; ao final,
transportar o conteúdo para o modelo do professor.

## Módulo 1 — Objetivos do estudo
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 1a | População ou distribuição sobre a qual a afirmação é feita | | Métodos §2.1; README §1 |
| 1b | Justificativa da escolha dessa população | | Introdução |
| 1c | Justificativa do uso de ML | | Introdução; Métodos §2.5 |

## Módulo 2 — Reprodutibilidade computacional
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 2a | Conjunto de dados identificado (link/DOI) | | README §2; `docs/dicionario_de_dados.md` |
| 2b | Código identificado (link/DOI) | | Repositório + tag de versão / DOI Zenodo |
| 2c | Infraestrutura computacional | | `docs/ambiente.md` |
| 2d | README com instruções | | `README.md` §3 |
| 2e | Script de reprodução | | `run_all.sh` / `Makefile` |

## Módulo 3 — Qualidade dos dados
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 3a | Fontes, período, processo de coleta | | Métodos §2.2 |
| 3b | Distribuição/conjunto amostrado | | Métodos §2.1 |
| 3c | Adequação dos dados à tarefa | | Métodos §2.2 |
| 3d | Definição do alvo + estatísticas descritivas | | Métodos §2.4; Tabela 1 |
| 3e | Número de amostras | | Tabela 1 |
| 3f | Percentual de ausentes por classe | | Tabela 2 |
| 3g | Representatividade | | Discussão (limitações) |

## Módulo 4 — Pré-processamento
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 4a | Amostras excluídas e justificativa | | Métodos §2.3; `docs/decisoes.md` D06 |
| 4b | Amostras impossíveis ou corrompidas | | Métodos §2.3; D05, D06 |
| 4c | Todas as transformações do bruto ao modelo | | Métodos §2.3; `src/features/` |

## Módulo 5 — Modelagem
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 5a | Modelos treinados, atributos, função de perda | | Métodos §2.5; Tabela 3 |
| 5b | Justificativa dos tipos de modelo | | Métodos §2.5 |
| 5c | Método de avaliação (split / CV) | | Métodos §2.6; D07 |
| 5d | Método de seleção do modelo reportado | | Métodos §2.6 |
| 5e | Ajuste de hiperparâmetros (intervalos, método, finais) | | Métodos §2.5; Apêndice A |
| 5f | Baselines apropriados | | Métodos §2.5; Tabela 4 |

## Módulo 6 — Vazamento de dados
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 6a | Pré-processamento usa só o treino | | Métodos §2.3; D04 |
| 6b | Dependências/duplicidades treino–teste | | Métodos §2.6; D07 |
| 6c | Legitimidade de cada atributo | | Métodos §2.4; Tabela de features |

## Módulo 7 — Métricas e incerteza
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 7a | Métricas apresentadas e adequação da métrica de seleção | | Métodos §2.7; Resultados §3.2 |
| 7b | Estimativas de incerteza e como foram calculadas | | Resultados §3.2 (bootstrap em blocos) |
| 7c | Testes estatísticos e premissas | | Resultados §3.3 ou N/A |

## Módulo 8 — Generalização e limitações
| Item | Questão | Situação | Onde está / o que falta |
|---|---|---|---|
| 8a | Evidências de validade externa | | Resultados §3.4 (teste 2023–2024) |
| 8b | Contextos em que os achados não valem | | Discussão |
