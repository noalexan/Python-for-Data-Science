from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's alive status to False."""
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark character, inheriting from Character."""

    def __init__(self, first_name: str, is_alive=True):
        """Initialize a Stark character with a first name and alive status."""
        super().__init__(first_name, is_alive)


def main() -> None:
    """Main function to demonstrate the usage of Stark class."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
