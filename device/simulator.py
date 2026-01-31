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
        temp = self.temp_sensor.read()
        hum = self.humidity_sensor.read()

        data = {
            "device_id": self.device_id,
            "timestamp": int(time.time())
        }

        if temp is not None:
            data["temperature"] = temp
        else:
            data["sensor_error"] = "TEMP_SENSOR_FAIL"

        if hum is not None:
            data["humidity"] = hum
        else:
            data["sensor_error"] = "HUMIDITY_SENSOR_FAIL"

        return data


    def edge_alerts(self, data):
        alerts = []

        if "temperature" in data and data["temperature"] > 35:
            alerts.append("EDGE_HIGH_TEMP")

        return alerts


    def run(self):
        print("Connecting to MQTT broker...", flush=True)
        self.mqtt.connect()
        print("Device running...", flush=True)

        while True:
            data = self.sample_sensors()

            edge_alerts = self.edge_alerts(data)
            if edge_alerts:
                data["edge_alerts"] = edge_alerts

            print("Publishing:", data, flush=True)
            self.mqtt.publish(MQTT_TOPIC, data)

            time.sleep(SAMPLING_INTERVAL_SEC)


if __name__ == "__main__":
    device = IoTDeviceSimulator()
    device.run()
