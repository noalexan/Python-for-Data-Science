from S1E9 import Character


class Baratheon(Character):
    """Represents a character from House Baratheon in Game of Thrones."""

    def __init__(
        self,
        first_name: str,
        is_alive=True,
        family_name="Baratheon",
        eyes="brown",
        hairs="dark",
    ):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)

        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return "Vector: {}".format(
            (self.family_name, self.eyes, self.hairs)
        )

    def __repr__(self) -> str:
        """Return a string representation of the Baratheon character."""
        return "Vector: {}".format(
            (self.family_name, self.eyes, self.hairs)
        )


class Lannister(Character):
    """Represents a character from House Lannister in Game of Thrones."""

    def __init__(
        self,
        first_name: str,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light",
    ):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)

        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(
        first_name: str,
        is_alive=True,
        family_name="Lannister",
        eyes="blue",
        hairs="light",
    ):
        """Create and return a new Lannister character."""
        return Lannister(first_name, is_alive, family_name, eyes, hairs)

    def __str__(self) -> str:
        """Return a string representation of the Lannister character."""
        return "Vector: {}".format(
            (self.family_name, self.eyes, self.hairs)
        )

    def __repr__(self) -> str:
        """Return a string representation of the Lannister character."""
        return "Vector: {}".format(
            (self.family_name, self.eyes, self.hairs)
        )


def main():
    """Demonstrate the usage of Baratheon and Lannister classes."""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)

    print("---")

    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)

    print("---")

    Jaine = Lannister.create_lannister("Jaine", True)
    print(
        "Name : {}, Alive : {}".format(
            (Jaine.first_name, type(Jaine).__name__), Jaine.is_alive
        )
    )


if __name__ == "__main__":
    main()
