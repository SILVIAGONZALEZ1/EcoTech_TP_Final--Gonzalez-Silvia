from django.shortcuts import render

from ejercicio_3_auditoria_web.emisiones import obtener_metricas_consumo


REGISTROS_CONSUMO = [
    {"planta": "Planta Norte", "consumo_kwh": 1250},
    {"planta": "Planta Sur", "consumo_kwh": 980},
    {"planta": "Planta Norte", "consumo_kwh": 430},
]


def vista_panel_sustentabilidad(request):
    contexto = obtener_metricas_consumo(REGISTROS_CONSUMO)
    return render(request, "sustentabilidad/panel.html", contexto)
