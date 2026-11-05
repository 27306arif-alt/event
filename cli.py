from registration import RegistrationError, RegistrationService


class RegistrationCLI:
    def __init__(self, service: RegistrationService = None):
        self.service = service or RegistrationService()

    def add_registration(self) -> None:
        name = input("Student name: ")
        registration_number = input("Registration number: ")
        workshop = input("Workshop: ")
        try:
            registration = self.service.register(name, registration_number, workshop)
            print("\nSuccess: registration completed.")
            print(registration)
        except RegistrationError as error:
            print(f"\nError: {error}")

    def list_registrations(self) -> None:
        registrations = self.service.list_registrations()
        if not registrations:
            print("\nNo registrations found.")
            return
        print("\nRegistered participants:")
        for index, registration in enumerate(registrations, start=1):
            print(f"{index}. {registration}")

    def run(self) -> None:
        while True:
            print("\nCampus Event Registration System")
            print("1. Register student")
            print("2. List registrations")
            print("3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.add_registration()
            elif choice == "2":
                self.list_registrations()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
