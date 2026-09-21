"""Testes das funções críticas — as que, se erradas, invalidam o estudo."""
import pandas as pd

from src.features.alvo import aplicar_alvo, estimar_climatologia


def test_climatologia_usa_apenas_treino():
    treino = pd.DataFrame({
        "celula_id": ["a", "a", "a"],
        "mes": [9, 9, 9],
        "focos": [100, 200, 300],
    })
    clim = estimar_climatologia(treino)
    assert clim.loc[0, "climatologia_mes"] == 200


def test_pico_exige_minimo_absoluto():
    painel = pd.DataFrame({
        "celula_id": ["a"], "mes": [9], "focos": [10],
    })
    clim = pd.DataFrame({"celula_id": ["a"], "mes": [9], "climatologia_mes": [2.0]})
    out = aplicar_alvo(painel, clim, limiar_razao=1.44,
                       min_focos_absoluto=30, meses_considerados=[5, 6, 7, 8, 9, 10])
    assert out.loc[0, "pico"] == 0  # razão 5x, mas volume irrelevante
