import threading
from simulator import IoTDeviceSimulator

NUM_DEVICES = 5  # start small, increase later

def run_device(device_id):
    device = IoTDeviceSimulator()
    device.device_id = device_id
    device.run()

threads = []

for i in range(NUM_DEVICES):
    device_id = f"device-{i+1}"
    t = threading.Thread(target=run_device, args=(device_id,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
