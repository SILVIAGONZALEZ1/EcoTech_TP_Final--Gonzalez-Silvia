from pathlib import Path

from ejercicio_2_productos.dispositivos import (
    DispositivoEcologico,
    GestorInventario,
    PanelSolar,
    StockInvalidoError,
)


def main() -> None:
    panel = PanelSolar("Solar Eco 400", stock=12, potencia_w=400, eficiencia=21.5)
    cargador = DispositivoEcologico("Cargador Verde", "Accesorios", stock=30)

    try:
        panel.stock = -3
    except StockInvalidoError as error:
        print(f"Asignación rechazada correctamente: {error}")

    catalogo = [panel, cargador]
    for dispositivo in catalogo:
        print(dispositivo.ficha_tecnica())

    ruta = Path(__file__).with_name("catalogo_ecotech.json")
    GestorInventario.guardar_catalogo_json(catalogo, ruta)
    print(f"Catálogo exportado a: {ruta}")


if __name__ == "__main__":
    main()
