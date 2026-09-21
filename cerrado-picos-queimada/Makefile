.PHONY: all data painel features train evaluate figuras test clean

PY = python

all: data painel features train evaluate figuras

data:
	$(PY) -m src.data.download_inpe
	$(PY) -m src.data.download_inmet

painel:
	$(PY) -m src.features.build_painel

features:
	$(PY) -m src.features.build_features

train:
	$(PY) -m src.models.train

evaluate:
	$(PY) -m src.evaluation.evaluate

figuras:
	$(PY) -m src.visualization.figuras_artigo

test:
	pytest -q

clean:
	rm -rf data/interim/* data/processed/* results/models/*
