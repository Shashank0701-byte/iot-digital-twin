import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from alert_engine import check_alerts
from database import init_db, insert_telemetry

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)
    if "temperature" in data and "humidity" in data:
        alerts = check_alerts(data)
        if alerts:
            print("🚨 CLOUD ALERTS:", alerts)
    else:
        print("⚠️ Incomplete data from", data["device_id"])

    insert_telemetry(data)

client = mqtt.Client(
    protocol=mqtt.MQTTv311,
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

init_db()
print("Cloud subscriber running with DB storage...")
client.loop_forever()
