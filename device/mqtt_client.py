import json
import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT

class MQTTClient:
    def __init__(self, client_id):
        self.client = mqtt.Client(
            client_id=client_id,
            protocol=mqtt.MQTTv311,
            callback_api_version=mqtt.CallbackAPIVersion.VERSION1
        )

    def connect(self):
        self.client.on_connect = lambda c, u, f, rc: print("MQTT connected with code", rc)
        self.client.connect(MQTT_BROKER, MQTT_PORT, 60)
        self.client.loop_start()

    def publish(self, topic, payload):
        self.client.publish(topic, json.dumps(payload))
