class StudentRegistration:
    """Represents one student workshop registration."""

    def __init__(self, name: str, registration_number: str, workshop: str):
        self._name = name.strip()
        self._registration_number = registration_number.strip()
        self._workshop = workshop.strip()

    @property
    def name(self) -> str:
        return self._name

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @property
    def workshop(self) -> str:
        return self._workshop

    def __str__(self) -> str:
        return (
            f"Name: {self.name} | Registration No: {self.registration_number} "
            f"| Workshop: {self.workshop}"
        )
