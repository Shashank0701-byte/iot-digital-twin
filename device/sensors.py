import random
import time

class TemperatureSensor:
    def __init__(self, base=25.0):
        self.base = base

    def read(self):
        if random.random() < 0.05:  # 5% failure
            return None

        noise = random.uniform(-0.5, 0.5)
        self.base += random.uniform(-0.05, 0.05)
        return round(self.base + noise, 2)


class HumiditySensor:
    def __init__(self, base=60.0):
        self.base = base

    def read(self):
        noise = random.uniform(-1, 1)
        self.base += random.uniform(-0.1, 0.1)
        return round(max(0, min(100, self.base + noise)), 2)
