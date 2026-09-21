# Fluxo de trabalho da dupla

## Branches
- `main` — sempre funcional. Nada é commitado direto aqui.
- `feat/<assunto>` — uma frente de trabalho por branch (`feat/painel-grade`,
  `feat/baselines`, `docs/metodos`).
- Integração por Pull Request, com revisão da outra pessoa antes do merge.

## Mensagens de commit
Formato curto e previsível:

```
feat: constrói painel célula x mês
fix: corrige defasagem que incluía o mês previsto
docs: escreve seção Métodos 2.3
exp: testa grade de 0.5 grau
```

## Divisão sugerida
- Pessoa A: `src/data`, `src/features`, painel, reprodutibilidade, `docs/ambiente.md`.
- Pessoa B: revisão de literatura, `docs/artigo/`, figuras, `docs/decisoes.md`.
- As duas: modelagem, avaliação e checklist REFORMS.

## Notebooks
Notebooks geram conflitos difíceis de resolver. Regras:
1. Cada pessoa é dona dos seus notebooks; não editar o do outro sem avisar.
2. Limpar as saídas antes de commitar (`Kernel > Restart & Clear Output`).
3. Código que for reutilizado migra para `src/`.

## Definição de pronto
Uma etapa só está pronta quando: o código roda do zero, a decisão está em
`docs/decisoes.md`, e a linha correspondente do `docs/reforms_checklist.md` foi
atualizada.
