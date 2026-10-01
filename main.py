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

    def toggle_status(self):
        """Växlar status mellan online och offline."""
        if self.status == "offline":
            self.status = "online"
        else:
            self.status = "offline"


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

    def search(self, term):
        """Returnerar en lista med enheter där sökordet finns i namn, typ eller plats."""
        term = term.lower()
        results = []

        for device in self.devices:
            if (term in device.name.lower()
                    or term in device.device_type.lower()
                    or term in device.location.lower()):
                results.append(device)

        return results

    def find_by_id(self, device_id):
        """Returnerar enheten med givet id, eller None om den inte finns."""
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None

    def remove_device(self, device_id):
        """Tar bort enheten med givet id. Returnerar den borttagna enheten, eller None."""
        device = self.find_by_id(device_id)
        if device is not None:
            self.devices.remove(device)
        return device


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


def print_menu():
    """Skriver ut huvudmenyn."""
    print("\n--- IOT-REGISTER ---")
    print("1. Lägg till enhet")
    print("2. Visa alla enheter")
    print("3. Sök enhet")
    print("4. Ändra status")
    print("5. Ta bort enhet")
    print("6. Avsluta")


def add_device_menu(registry):
    """Frågar användaren om uppgifter och lägger till en ny enhet."""
    name = read_nonempty("Namn: ")
    device_type = read_nonempty("Typ (t.ex. sensor, gateway): ")
    location = read_nonempty("Plats: ")

    device = registry.add_device(name, device_type, location)
    print(f"Tillagd: {device}")


def search_menu(registry):
    """Frågar efter ett sökord och visar matchande enheter."""
    term = read_nonempty("Sökord (namn, typ eller plats): ")
    results = registry.search(term)

    if not results:
        print(f"Inga enheter matchade '{term}'.")
        return

    print(f"Hittade {len(results)} enhet(er):")
    for device in results:
        print(device)


def change_status_menu(registry):
    """Låter användaren välja en enhet och växla dess status."""
    if not registry.devices:
        print("Inga enheter registrerade.")
        return

    registry.show_all()
    device_id = read_int("Ange id: ", 1, registry.next_id - 1)
    device = registry.find_by_id(device_id)

    if device is None:
        print(f"Ingen enhet med id {device_id}.")
        return

    device.toggle_status()
    print(f"Uppdaterad: {device}")


def remove_device_menu(registry):
    """Låter användaren välja en enhet och ta bort den efter bekräftelse."""
    if not registry.devices:
        print("Inga enheter registrerade.")
        return

    registry.show_all()
    device_id = read_int("Ange id: ", 1, registry.next_id - 1)
    device = registry.find_by_id(device_id)

    if device is None:
        print(f"Ingen enhet med id {device_id}.")
        return

    answer = read_nonempty(f"Ta bort {device.name}? (j/n): ").lower()
    if answer != "j":
        print("Avbrutet.")
        return

    registry.remove_device(device_id)
    print(f"Borttagen: {device}")


def main():
    registry = DeviceRegistry()

    while True:
        print_menu()
        choice = read_int("Välj (1-6): ", 1, 6)

        if choice == 1:
            add_device_menu(registry)
        elif choice == 2:
            registry.show_all()
        elif choice == 3:
            search_menu(registry)
        elif choice == 4:
            change_status_menu(registry)
        elif choice == 5:
            remove_device_menu(registry)
        else:
            print("Hej då!")
            break


if __name__ == "__main__":
    main()