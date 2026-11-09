import math
from collections.abc import Iterable, Mapping
from typing import Any


def calcular_emisiones_carbono(
    consumo_kwh: float,
    factor_emision: float = 0.4,
) -> float:
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    if not math.isfinite(consumo_kwh) or not math.isfinite(factor_emision):
        raise ValueError("El consumo y el factor deben ser valores finitos.")
    if factor_emision < 0:
        raise ValueError("El factor de emisión no puede ser negativo.")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    emisiones_totales = 0.0
    consumo_por_planta: dict[str, float] = {}

    for registro in registros:
        planta = registro.get("planta")
        if not isinstance(planta, str) or not planta.strip():
            raise ValueError("Cada registro debe incluir el nombre de la planta.")
        consumo = float(registro["consumo_kwh"])
        emisiones_totales += calcular_emisiones_carbono(consumo)
        nombre_planta = planta.strip()
        consumo_por_planta[nombre_planta] = (
            consumo_por_planta.get(nombre_planta, 0.0) + consumo
        )

    if consumo_por_planta:
        planta_mayor = max(consumo_por_planta, key=consumo_por_planta.get)
        consumo_mayor = consumo_por_planta[planta_mayor]
    else:
        planta_mayor = None
        consumo_mayor = 0.0

    return {
        "total_emisiones_kg": emisiones_totales,
        "planta_mayor_consumo": planta_mayor,
        "consumo_mayor_kwh": consumo_mayor,
        "consumo_por_planta": consumo_por_planta,
    }
