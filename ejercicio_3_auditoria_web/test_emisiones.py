import unittest

from ejercicio_3_auditoria_web.emisiones import (
    calcular_emisiones_carbono,
    obtener_metricas_consumo,
)


class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_con_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_calculo_con_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(50, 0.25), 12.5)

    def test_consumo_negativo_eleva_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)

    def test_metricas_agregan_emisiones_y_consumo_por_planta(self):
        registros = [
            {"planta": "Norte", "consumo_kwh": 100},
            {"planta": "Sur", "consumo_kwh": 150},
            {"planta": "Norte", "consumo_kwh": 50},
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertEqual(metricas["total_emisiones_kg"], 120.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Norte")
        self.assertEqual(metricas["consumo_mayor_kwh"], 150.0)

    def test_metricas_sin_registros(self):
        metricas = obtener_metricas_consumo([])
        self.assertEqual(metricas["total_emisiones_kg"], 0.0)
        self.assertIsNone(metricas["planta_mayor_consumo"])


if __name__ == "__main__":
    unittest.main()
