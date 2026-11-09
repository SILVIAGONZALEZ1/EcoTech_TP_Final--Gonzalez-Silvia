from ejercicio_1_sensores.sensores import (
    generar_resumen_sensores,
    limpiar_registro_sensor,
)


def main() -> None:
    registros_raw = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "31 °C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-003", "temperatura": "22,0", "ubicacion": ""},
    ]
    sensores = [limpiar_registro_sensor(registro) for registro in registros_raw]
    alertas, promedio = generar_resumen_sensores(sensores, umbral_temperatura=28.0)

    print("=== Reporte de sensores EcoTech ===")
    print(f"Sensores procesados: {len(sensores)}")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Sensores en alerta: {', '.join(alertas) if alertas else 'Ninguno'}")


if __name__ == "__main__":
    main()
