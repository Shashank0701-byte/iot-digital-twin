import time
from sensors import TemperatureSensor, HumiditySensor
from config import DEVICE_ID, SAMPLING_INTERVAL_SEC, MQTT_TOPIC
from mqtt_client import MQTTClient

class IoTDeviceSimulator:
    def __init__(self):
        self.device_id = DEVICE_ID
        self.temp_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()
        self.mqtt = MQTTClient(client_id=self.device_id)

    def sample_sensors(self):
        return {
            "device_id": self.device_id,
            "timestamp": int(time.time()),
            "temperature": self.temp_sensor.read(),
            "humidity": self.humidity_sensor.read()
        }

    def run(self):
        print("Connecting to MQTT broker...")
        self.mqtt.connect()
        print("Device running...")

        while True:
            data = self.sample_sensors()
            print("Publishing:", data)
            self.mqtt.publish(MQTT_TOPIC, data)
            time.sleep(SAMPLING_INTERVAL_SEC)


if __name__ == "__main__":
    device = IoTDeviceSimulator()
    device.run()
