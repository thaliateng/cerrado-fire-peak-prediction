#!/usr/bin/env bash
# Script de reprodução completa (REFORMS 2e).
# Uso: bash run_all.sh
set -euo pipefail

echo "[1/6] Download dos dados brutos"
python -m src.data.download_inpe
python -m src.data.download_inmet

echo "[2/6] Construção do painel célula x mês"
python -m src.features.build_painel

echo "[3/6] Features de defasagem e variável-alvo"
python -m src.features.build_features

echo "[4/6] Treino dos baselines e modelos"
python -m src.models.train

echo "[5/6] Avaliação e incerteza"
python -m src.evaluation.evaluate

echo "[6/6] Figuras e tabelas do artigo"
python -m src.visualization.figuras_artigo

echo "Concluído. Saídas em results/."
