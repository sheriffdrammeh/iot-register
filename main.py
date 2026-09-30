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


def read_nonempty(prompt):
    """Frågar tills användaren skriver något som inte är tomt."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Fältet får inte vara tomt. Försök igen.")


def read_int(prompt, min_value, max_value):
    """Frågar tills användaren skriver ett heltal mellan min_value och max_value."""
    while True:
        text = input(prompt).strip()
        try:
            number = int(text)
        except ValueError:
            print("Ange ett heltal.")
            continue

        if min_value <= number <= max_value:
            return number
        print(f"Ange ett tal mellan {min_value} och {max_value}.")


def main():
    name = read_nonempty("Namn: ")
    choice = read_int("Välj 1-5: ", 1, 5)
    print(f"Du skrev {name} och valde {choice}")


if __name__ == "__main__":
    main()