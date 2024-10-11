def square(x: int | float) -> int | float:
    """Return the square of the input number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that applies the given function repeatedly."""
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner


def main():
    """Execute the main program logic."""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
