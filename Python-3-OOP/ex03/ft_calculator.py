import sys


class calculator:
    """A calculator class for performing operations on lists of numbers."""

    def __init__(self, object):
        """Initialize the calculator with a list of numbers."""
        self.numbers = object

    def __add__(self, object) -> None:
        """Add a value to each number in the list."""
        self.numbers = [number + object for number in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """Multiply each number in the list by a value."""
        self.numbers = [number * object for number in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """Subtract a value from each number in the list."""
        self.numbers = [number - object for number in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """Divide each number in the list by a value."""
        if object == 0:
            print("Unable to divise by 0", file=sys.stderr)
        self.numbers = [number / object for number in self.numbers]
        print(self.numbers)


def main() -> None:
    """Demonstrate the usage of the calculator class."""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
