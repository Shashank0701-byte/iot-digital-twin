import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from alert_engine import check_alerts

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)

    alerts = check_alerts(data)
    if alerts:
        print("🚨 ALERTS:", alerts)

client = mqtt.Client(
    protocol=mqtt.MQTTv311,
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

print("Cloud subscriber running...")
client.loop_forever()
