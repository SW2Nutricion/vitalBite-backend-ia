"""Compatibilidad: use app.application.use_cases.risk_prediction."""
from app.application.use_cases.risk_prediction import (
    RiskPredictionService,
    InsufficientDataError,
    ModelNotLoadedError,
    _identify_critical_factors,
)

__all__ = [
    "RiskPredictionService",
    "InsufficientDataError",
    "ModelNotLoadedError",
    "_identify_critical_factors",
]
