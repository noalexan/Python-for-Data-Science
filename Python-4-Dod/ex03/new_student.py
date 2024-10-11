import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character lowercase string ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with name, surname, active status, login, and ID."""
    name: str = field()
    surname: str = field()
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Initialize login using the first letter of name and full surname."""
        self.login = self.name[0] + self.surname


def main():
    """Create a Student instance and print it to demonstrate the dataclass."""

    student = Student(name="Edward", surname="agle")
    print(student)

    try:
        Student(name="Edward", surname="agle", login="toto")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
