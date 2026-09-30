class Device:
    """Representerar en IoT-enhet."""

    def __init__(self, device_id, name, device_type, location):
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.location = location
        self.status = "offline"

    def __str__(self):
        return f"[{self.device_id}] {self.name} ({self.device_type}) – {self.location} – {self.status}"


def main():
    d = Device(1, "Temp-sensor", "sensor", "Kök")
    print(d)


if __name__ == "__main__":
    main()