class calculator:
    """A class containing vector operations."""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        result = sum([a * b for a, b in zip(V1, V2)])
        print(result)
        return result

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise and print the result."""
        list = [a + b for a, b in zip(V1, V2)]
        print(list)
        return list

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors element-wise and print the result."""
        list = [a - b for a, b in zip(V1, V2)]
        print(list)
        return list


def main() -> None:
    """Execute vector operations using the calculator class."""
    a = [5, 10, 2]
    b = [2, 4, 3]

    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
