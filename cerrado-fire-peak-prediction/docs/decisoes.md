# Registro de decisões metodológicas

Cada decisão recebe data, alternativa escolhida, alternativas descartadas e
justificativa. Este arquivo alimenta diretamente a seção Métodos do artigo e as
respostas do checklist REFORMS.

---

## D01 — Unidade de análise: célula de grade × mês
**Data:** <aaaa-mm-dd>
**Decisão:** adotar célula de 1° × 1° em vez do bioma inteiro.
**Descartado:** bioma × mês (120 observações, 12 positivos).
**Justificativa:** amostra insuficiente para ML e para estimativas de incerteza
confiáveis; a desagregação também permite associar cada região à estação
meteorológica mais próxima, atacando a limitação de representatividade climática.
**Itens REFORMS:** 1a, 3g, 5c.

## D02 — Horizonte de previsão de um mês
**Data:** <aaaa-mm-dd>
**Decisão:** prever o mês *t+1* com informação disponível até o fim de *t*.
**Justificativa:** usar o clima do próprio mês previsto tornaria o estudo
explicativo, não preditivo, e configuraria vazamento temporal.
**Itens REFORMS:** 6a, 6c.

## D03 — Definição do alvo
**Data:** <aaaa-mm-dd>
**Decisão:** pico = razão acima do percentil 90 da climatologia da célula **e**
mínimo absoluto de focos, restrito aos meses de maio a outubro.
**Descartado:** razão pura sobre os 12 meses.
**Justificativa:** sem o mínimo absoluto, meses da estação úmida com poucas
centenas de focos entram como pico e competem com setembro, o que contradiz o
problema ambiental declarado.
**Itens REFORMS:** 3d, 1a.

## D04 — Climatologia e limiar estimados só no treino
**Data:** <aaaa-mm-dd>
**Justificativa:** calcular a média histórica sobre a série inteira faria o
rótulo de 2016 depender de 2024.
**Itens REFORMS:** 6a.

## D05 — Tratamento dos ausentes estruturais do INMET
**Data:** <aaaa-mm-dd>
**Decisão:** agregar por mês usando apenas os registros válidos de cada variável;
documentar a cobertura mensal efetiva.
**Itens REFORMS:** 4b, 4c.

## D06 — Focos fora da caixa retangular lat/lon
**Data:** <aaaa-mm-dd>
**Decisão:** manter os 504 registros (~0,08%). A investigação mostrou enclaves
reais de Cerrado no norte do PR/SP e no oeste do MT, corretamente rotulados pelo
INPE. Passar a usar o polígono oficial do IBGE em vez da caixa retangular.
**Itens REFORMS:** 4a, 4b.

## D07 — Divisão temporal e dependência espacial
**Data:** <aaaa-mm-dd>
**Decisão:** treino 2015–2021, validação 2022, teste 2023–2024; reportar também
origem móvel. Bootstrap em blocos anuais para intervalos.
**Justificativa:** picos concentrados em 2015 e 2024; células vizinhas no mesmo
mês são correlacionadas, o que invalida reamostragem simples.
**Itens REFORMS:** 5c, 6b, 7b.
