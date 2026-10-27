"""Endpoint CU10 — POST /api/v1/risk-prediction (Random Forest).

Controlador delgado: valida con Pydantic, delega en el servicio y deja que los
errores de dominio (InsufficientDataError → 422, ModelNotLoadedError → 503) los
mapeen los handlers globales registrados en ``main.py``.
"""

from fastapi import APIRouter, Depends

from app.application.use_cases.risk_prediction import RiskPredictionService
from app.core.security import verify_api_key
from app.infrastructure.ml.risk_model_provider import CachedRiskModelProvider
from app.interfaces.http.schemas.risk_prediction import (
    RiskPredictionRequest,
    RiskPredictionResponse,
)

router = APIRouter()


def get_service() -> RiskPredictionService:
    return RiskPredictionService(CachedRiskModelProvider())


@router.post(
    "",
    response_model=RiskPredictionResponse,
    summary="Predecir riesgo nutricional con Random Forest",
    dependencies=[Depends(verify_api_key)],
)
def predict_risk(
    request: RiskPredictionRequest,
    service: RiskPredictionService = Depends(get_service),
) -> RiskPredictionResponse:
    return service.predict(request)
