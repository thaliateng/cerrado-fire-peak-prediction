# Esqueleto do artigo (IMRaD)

**Título provisório:** Previsão de anomalias mensais de focos de queimada no
Cerrado com aprendizado de máquina e dados climáticos antecedentes (2015–2024)

**Palavras-chave:** Cerrado; queimadas; aprendizado de máquina; anomalia
climática; sensoriamento remoto

## Resumo (200–250 palavras)
Problema · objetivo · dados e método · principais resultados · conclusão.
Escrever por último.

## 1. Introdução
- 1.1 Estabelecimento do território: importância do Cerrado, escala das queimadas.
- 1.2 Estabelecimento do nicho: o que a literatura já faz (monitoramento, risco de
  fogo) e o que falta (previsão de anomalia em escala sub-regional com dados
  públicos abertos).
- 1.3 Ocupação do nicho: objetivo geral e contribuições.

## 2. Método
- 2.1 Área de estudo e unidade de análise
- 2.2 Fontes de dados (INPE, INMET) e período
- 2.3 Pré-processamento (filtros, exclusões, agregação, ausentes)
- 2.4 Construção da variável-alvo e das features defasadas
- 2.5 Modelos, baselines e ajuste de hiperparâmetros
- 2.6 Estratégia de validação temporal e controle de vazamento
- 2.7 Métricas e estimativas de incerteza

## 3. Resultados
- 3.1 Caracterização dos dados e análise exploratória (sazonalidade, variação
  interanual, concentração no MATOPIBA, correlações entre anomalias)
- 3.2 Desempenho dos modelos e comparação com os baselines
- 3.3 Importância das variáveis
- 3.4 Análise de erro: quais picos o modelo perdeu

## 4. Discussão
Interpretação dos achados · comparação com a literatura · limitações (foco de
calor não é incêndio confirmado, nuvens, série de 10 anos, densidade de estações)
· implicações práticas.

## 5. Conclusão
Resposta direta ao objetivo, sem introduzir resultado novo.

## Referências
Ver `referencias.bib`.

## Apêndices
- A: grade de hiperparâmetros testada
- B: checklist REFORMS preenchido
