from django.urls import path

from ejercicio_3_auditoria_web.views import vista_panel_sustentabilidad


urlpatterns = [
    path("", vista_panel_sustentabilidad, name="panel_sustentabilidad"),
]
