"""Compatibilidad: los handlers HTTP viven en app.interfaces.http."""
from app.domain.exceptions import (
    CoreServiceError,
    InsufficientDataError,
    InsufficientPatientsError,
    ModelNotLoadedError,
)
from app.interfaces.http.exception_handlers import (
    core_service_handler,
    insufficient_data_handler,
    insufficient_patients_handler,
    model_not_loaded_handler,
)

__all__ = [
    "CoreServiceError",
    "InsufficientDataError",
    "InsufficientPatientsError",
    "ModelNotLoadedError",
    "core_service_handler",
    "insufficient_data_handler",
    "insufficient_patients_handler",
    "model_not_loaded_handler",
]
