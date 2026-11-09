import unittest

from ejercicio_1_sensores.sensores import (
    generar_resumen_sensores,
    limpiar_registro_sensor,
)


class TestSensores(unittest.TestCase):
    def test_limpia_texto_y_unidad_de_temperatura(self):
        registro = limpiar_registro_sensor(
            {"sensor_id": " SENSOR-001 ", "temperatura": "24.5°C", "ubicacion": " Norte "}
        )
        self.assertEqual(
            registro,
            {"sensor_id": "SENSOR-001", "temperatura": 24.5, "ubicacion": "Norte"},
        )

    def test_ubicacion_por_defecto(self):
        registro = limpiar_registro_sensor(
            {"sensor_id": "S-2", "temperatura": 18}
        )
        self.assertEqual(registro["ubicacion"], "Ubicación no especificada")

    def test_rechaza_temperatura_invalida(self):
        with self.assertRaises(ValueError):
            limpiar_registro_sensor(
                {"sensor_id": "S-3", "temperatura": "sin dato"}
            )

    def test_resumen_alertas_y_promedio(self):
        sensores = [
            {"sensor_id": "S-1", "temperatura": 20.0},
            {"sensor_id": "S-2", "temperatura": 30.0},
        ]
        self.assertEqual(generar_resumen_sensores(sensores, 25), (["S-2"], 25.0))

    def test_resumen_vacio(self):
        self.assertEqual(generar_resumen_sensores([], 25), ([], 0.0))


if __name__ == "__main__":
    unittest.main()
