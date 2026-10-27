# Arquitectura DDD del microservicio IA

El microservicio está organizado por responsabilidades y no por librería:

```text
app/
├── domain/
│   └── exceptions.py
├── application/
│   ├── ports/
│   └── use_cases/
├── infrastructure/
│   └── ml/
├── interfaces/
│   └── http/
├── core/
└── models/
```

## Reglas de dependencia

1. `domain` no importa FastAPI, Pydantic, NumPy ni artefactos de ML.
2. `application` coordina casos de uso y define puertos; no conoce FastAPI.
3. `infrastructure` implementa puertos y encapsula TensorFlow, EasyOCR,
   scikit-learn y la carga desde disco.
4. `interfaces/http` convierte solicitudes HTTP en comandos de aplicación y
   respuestas en contratos Pydantic.
5. `core` contiene configuración y preocupaciones transversales; los handlers
   HTTP permanecen en `interfaces/http`.

## Casos de uso

- `application/use_cases/food_scan.py`: orquesta OCR/CNN y el semáforo
  nutricional.
- `application/use_cases/risk_prediction.py`: valida features, solicita los
  modelos mediante `RiskModelProvider` y construye la respuesta.
- `application/use_cases/segmentation.py`: valida el mínimo de pacientes y
  orquesta K-means/PCA.

## Compatibilidad

Los módulos históricos en `app/services`, `app/schemas` y `app/api/v1` son
fachadas de transición. Las rutas HTTP, los nombres de campos y los códigos
de error no cambian durante esta migración.
