"""Excepciones de negocio independientes de FastAPI y de la infraestructura."""


class InsufficientDataError(Exception):
    """El expediente no tiene suficientes features para predecir."""

    def __init__(self, missing_fields: list[str]):
        self.missing_fields = missing_fields
        super().__init__(f"Datos insuficientes. Campos faltantes: {missing_fields}")


class InsufficientPatientsError(Exception):
    """El tenant no tiene suficientes pacientes para ejecutar K-means."""

    def __init__(self, count: int, minimum: int):
        self.count = count
        self.minimum = minimum
        super().__init__(
            f"Se requieren al menos {minimum} pacientes. Se recibieron {count}."
        )


class ModelNotLoadedError(Exception):
    """Un artefacto de ML no está disponible para inferencia."""

    def __init__(self, model_path: str, reason: str | None = None):
        self.model_path = model_path
        self.reason = reason
        message = f"Modelo no disponible: {model_path}"
        if reason:
            message += f" ({reason})"
        super().__init__(message)


class CoreServiceError(Exception):
    """Falla al comunicarse con el backend Core."""

    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(detail)
