import math
import re
from collections.abc import Iterable, Mapping
from typing import Any


_TEMPERATURA_PATTERN = re.compile(
    r"^\s*([+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+))\s*(?:°?\s*[cC])?\s*$"
)


def limpiar_registro_sensor(registro_raw: Mapping[str, Any]) -> dict[str, Any]:
    """Devuelve un registro estandarizado o informa datos inválidos."""
    sensor_id = registro_raw.get("sensor_id")
    if not isinstance(sensor_id, str) or not sensor_id.strip():
        raise ValueError("El sensor_id debe ser un texto no vacío.")

    temperatura_raw = registro_raw.get("temperatura")
    if isinstance(temperatura_raw, bool) or temperatura_raw is None:
        raise ValueError("La temperatura debe ser un número válido.")
    if isinstance(temperatura_raw, (int, float)):
        temperatura = float(temperatura_raw)
    elif isinstance(temperatura_raw, str):
        match = _TEMPERATURA_PATTERN.fullmatch(temperatura_raw)
        if match is None:
            raise ValueError(f"Temperatura inválida: {temperatura_raw!r}.")
        temperatura = float(match.group(1).replace(",", "."))
    else:
        raise ValueError("La temperatura debe ser un número o texto numérico.")

    if not math.isfinite(temperatura):
        raise ValueError("La temperatura debe ser finita.")

    ubicacion_raw = registro_raw.get("ubicacion")
    ubicacion = (
        ubicacion_raw.strip()
        if isinstance(ubicacion_raw, str) and ubicacion_raw.strip()
        else "Ubicación no especificada"
    )
    return {
        "sensor_id": sensor_id.strip(),
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(
    lista_sensores_limpios: Iterable[Mapping[str, Any]],
    umbral_temperatura: float,
) -> tuple[list[str], float]:
    """Retorna IDs por encima del umbral y el promedio térmico."""
    temperaturas: list[float] = []
    sensores_alerta: list[str] = []
    for sensor in lista_sensores_limpios:
        temperatura = float(sensor["temperatura"])
        temperaturas.append(temperatura)
        if temperatura > umbral_temperatura:
            sensores_alerta.append(str(sensor["sensor_id"]))
    promedio = sum(temperaturas) / len(temperaturas) if temperaturas else 0.0
    return sensores_alerta, promedio
