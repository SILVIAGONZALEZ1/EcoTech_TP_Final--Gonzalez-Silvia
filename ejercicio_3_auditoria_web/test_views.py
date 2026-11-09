import os
import unittest

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "ejercicio_3_auditoria_web.settings"
)

try:
    import django

    django.setup()
    from django.test import Client

    DJANGO_AVAILABLE = True
except ModuleNotFoundError:
    DJANGO_AVAILABLE = False


@unittest.skipUnless(DJANGO_AVAILABLE, "Instale Django para probar la vista.")
class TestVistaPanelSustentabilidad(unittest.TestCase):
    def test_renderiza_panel_con_metricas(self):
        respuesta = Client().get("/")
        self.assertEqual(respuesta.status_code, 200)
        contenido = respuesta.content.decode("utf-8")
        self.assertIn("Panel de sustentabilidad", contenido)
        self.assertIn("1064.00", contenido)
        self.assertIn("kg CO₂", contenido)
        self.assertIn("Planta Norte", contenido)


if __name__ == "__main__":
    unittest.main()
