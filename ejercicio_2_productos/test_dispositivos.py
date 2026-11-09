import json
import tempfile
import unittest
from pathlib import Path

from ejercicio_2_productos.dispositivos import (
    DispositivoEcologico,
    GestorInventario,
    PanelSolar,
    StockInvalidoError,
)


class TestDispositivos(unittest.TestCase):
    def test_stock_negativo_es_rechazado_al_asignar(self):
        dispositivo = DispositivoEcologico("Batería", "Almacenamiento", 2)
        with self.assertRaises(StockInvalidoError):
            dispositivo.stock = -1
        self.assertEqual(dispositivo.stock, 2)

    def test_stock_no_entero_es_rechazado(self):
        with self.assertRaises(StockInvalidoError):
            DispositivoEcologico("Batería", "Almacenamiento", 1.5)

    def test_panel_personaliza_ficha_y_serializacion(self):
        panel = PanelSolar("Eco 400", 5, 400, 20.5)
        self.assertIn("Potencia: 400 W", panel.ficha_tecnica())
        self.assertEqual(panel.a_diccionario()["tipo"], "PanelSolar")

    def test_guarda_catalogo_json(self):
        catalogo = [PanelSolar("Eco 400", 5, 400, 20.5)]
        with tempfile.TemporaryDirectory() as directorio:
            archivo = Path(directorio) / "catalogo_ecotech.json"
            GestorInventario.guardar_catalogo_json(catalogo, archivo)
            datos = json.loads(archivo.read_text(encoding="utf-8"))
        self.assertEqual(datos[0]["nombre"], "Eco 400")
        self.assertEqual(datos[0]["potencia_w"], 400)


if __name__ == "__main__":
    unittest.main()
