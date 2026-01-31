def check_alerts(data):
    alerts = []

    if data["temperature"] > 30:
        alerts.append("HIGH_TEMPERATURE")

    if data["humidity"] > 75:
        alerts.append("HIGH_HUMIDITY")

    return alerts
