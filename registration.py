from models import StudentRegistration


class RegistrationError(Exception):
    pass


class RegistrationService:
    def __init__(self):
        self._registrations = []

    def register(self, name: str, registration_number: str, workshop: str) -> StudentRegistration:
        values = {
            "name": name,
            "registration number": registration_number,
            "workshop": workshop,
        }
        for field, value in values.items():
            if not value or not value.strip():
                raise RegistrationError(f"{field.capitalize()} is required.")

        normalized_number = registration_number.strip()
        if any(item.registration_number == normalized_number for item in self._registrations):
            raise RegistrationError("Duplicate registration number rejected.")

        registration = StudentRegistration(name, normalized_number, workshop)
        self._registrations.append(registration)
        return registration

    def list_registrations(self) -> list[StudentRegistration]:
        return list(self._registrations)
