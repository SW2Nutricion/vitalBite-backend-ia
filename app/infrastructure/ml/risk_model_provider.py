"""Adaptador del cargador de artefactos Random Forest."""

from typing import Any

from app.infrastructure.ml.model_loader import get_rf_model, get_rf_scaler


class CachedRiskModelProvider:
    def get_model(self) -> Any:
        return get_rf_model()

    def get_scaler(self) -> Any:
        return get_rf_scaler()
