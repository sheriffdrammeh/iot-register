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


class DeviceRegistry:
    """Håller reda på alla IoT-enheter i en lista."""

    def __init__(self):
        self.devices = []
        self.next_id = 1

    def add_device(self, name, device_type, location):
        device = Device(self.next_id, name, device_type, location)
        self.devices.append(device)
        self.next_id += 1
        return device

    def show_all(self):
        if not self.devices:
            print("Inga enheter registrerade.")
            return

        for device in self.devices:
            print(device)


def main():
    registry = DeviceRegistry()

    registry.show_all()

    registry.add_device("Temp-sensor", "sensor", "Kök")
    registry.add_device("Gateway", "gateway", "Hall")

    registry.show_all()


if __name__ == "__main__":
    main()