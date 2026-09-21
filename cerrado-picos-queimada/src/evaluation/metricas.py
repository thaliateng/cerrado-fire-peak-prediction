"""Métricas adequadas a classes desbalanceadas (REFORMS 7a)."""
from __future__ import annotations

import numpy as np
from sklearn.metrics import (average_precision_score, brier_score_loss, f1_score,
                             precision_score, recall_score)


def avaliar(y_true, y_prob, limiar: float = 0.5) -> dict[str, float]:
    y_pred = (np.asarray(y_prob) >= limiar).astype(int)
    return {
        "pr_auc": average_precision_score(y_true, y_prob),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "brier": brier_score_loss(y_true, y_prob),
    }
