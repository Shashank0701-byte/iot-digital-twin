import time
from sensors import TemperatureSensor, HumiditySensor
from config import DEVICE_ID, SAMPLING_INTERVAL_SEC

class IoTDeviceSimulator:
    def __init__(self):
        self.device_id = DEVICE_ID
        self.temp_sensor = TemperatureSensor()
        self.humidity_sensor = HumiditySensor()

    def sample_sensors(self):
        return {
            "device_id": self.device_id,
            "timestamp": int(time.time()),
            "temperature": self.temp_sensor.read(),
            "humidity": self.humidity_sensor.read()
        }

    def run(self):
        print("Starting IoT Device Simulator...")
        while True:
            data = self.sample_sensors()
            print("Telemetry:", data)
            time.sleep(SAMPLING_INTERVAL_SEC)


if __name__ == "__main__":
    device = IoTDeviceSimulator()
    device.run()
