"""Contrato para los modelos usados por el caso de uso de riesgo."""

from typing import Any, Protocol


class RiskModelProvider(Protocol):
    def get_model(self) -> Any:
        ...

    def get_scaler(self) -> Any:
        ...
