# Infraestrutura computacional (REFORMS 2c)

Preencher com os dados reais da máquina usada para gerar os resultados finais.

## Hardware
- Processador: <modelo, nº de núcleos>
- Memória RAM: <GB>
- GPU: <modelo ou "não utilizada">
- Armazenamento livre: <GB>

## Sistema operacional
- <ex.: Windows 11 24H2 / Ubuntu 24.04 LTS>

## Ambiente de software
- Python <versão exata: `python --version`>
- Gerenciador de ambiente: venv
- Pacotes: ver `requirements.txt`; a versão congelada da execução final está em
  `requirements-freeze.txt` (`pip freeze > requirements-freeze.txt`)

## Tempo de execução
| Etapa | Tempo aproximado |
|---|---|
| Download dos dados | |
| Construção do painel | |
| Features | |
| Treino + ajuste de hiperparâmetros | |
| Avaliação e figuras | |
| **Total (`make all`)** | |

## Semente aleatória
Definida em `config/params.yaml` (`projeto.seed`) e propagada para NumPy,
scikit-learn e LightGBM.
