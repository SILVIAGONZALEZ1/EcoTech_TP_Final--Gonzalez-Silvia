import json
from pathlib import Path
from typing import Any


class StockInvalidoError(ValueError):
    """Se intenta asignar una cantidad de stock inválida."""


class DispositivoEcologico:
    def __init__(self, nombre: str, categoria: str, stock: int) -> None:
        if not nombre.strip() or not categoria.strip():
            raise ValueError("El nombre y la categoría son obligatorios.")
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.stock = stock

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if isinstance(valor, bool) or not isinstance(valor, int) or valor < 0:
            raise StockInvalidoError("El stock debe ser un entero no negativo.")
        self._stock = valor

    def ficha_tecnica(self) -> str:
        return (
            f"{self.nombre} | Categoría: {self.categoria} | "
            f"Stock disponible: {self.stock}"
        )

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):
    def __init__(
        self,
        nombre: str,
        stock: int,
        potencia_w: int,
        eficiencia: float,
    ) -> None:
        super().__init__(nombre, "Panel solar", stock)
        if isinstance(potencia_w, bool) or not isinstance(potencia_w, int) or potencia_w <= 0:
            raise ValueError("La potencia debe ser un entero positivo.")
        if not 0 < eficiencia <= 100:
            raise ValueError("La eficiencia debe estar entre 0 y 100.")
        self.potencia_w = potencia_w
        self.eficiencia = float(eficiencia)

    def ficha_tecnica(self) -> str:
        return (
            f"{super().ficha_tecnica()} | Potencia: {self.potencia_w} W | "
            f"Eficiencia: {self.eficiencia:g}%"
        )

    def a_diccionario(self) -> dict[str, Any]:
        return {
            **super().a_diccionario(),
            "potencia_w": self.potencia_w,
            "eficiencia": self.eficiencia,
        }


class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(
        lista_dispositivos: list[DispositivoEcologico],
        ruta_archivo: str | Path,
    ) -> None:
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        catalogo = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        ruta.write_text(
            json.dumps(catalogo, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
