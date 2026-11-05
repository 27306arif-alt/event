# Campus Event Registration System

A lightweight Python command-line prototype for registering students for campus workshops.

## Project Structure

- `models.py` — `StudentRegistration` data model with encapsulated fields.
- `registration.py` — registration business logic, validation, duplicate prevention, listing, and searching.
- `cli.py` — text input/output and menu handling.
- `main.py` — application entry point.
- `tests/test_registration.py` — unit tests for registration behavior.

## Design Approach

Abstraction and modularity keep each part focused: data representation, rules, and presentation can change independently. This prototype follows separation of concerns; the registration service acts as a repository/service-style boundary around workshop registrations.
