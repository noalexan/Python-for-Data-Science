from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represents a king with traits from both Baratheon and Lannister."""

    def set_eyes(self, eyes: str):
        """Sets the eye color of the king."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Sets the hair color of the king."""
        self.hairs = hairs

    def get_eyes(self):
        """Returns the eye color of the king."""
        return self.eyes

    def get_hairs(self):
        """Returns the hair color of the king."""
        return self.hairs


def main() -> None:
    """Main function to demonstrate the King class functionality."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
