import sys
from typing import List


def ft_mean(*numbers: float) -> float:
    """Calculate the arithmetic mean of the given numbers."""
    return sum(numbers) / len(numbers)


def ft_median(*numbers: float) -> float:
    """Calculate the median of the given numbers."""
    num_list = list(numbers)
    num_list.sort()
    return num_list[int(len(num_list) / 2)]


def ft_quartile(*numbers: float) -> List[float]:
    """Calculate the first and third quartiles of the given numbers."""
    num_list = list(numbers)
    num_list.sort()
    return [
        num_list[int(len(num_list) * 0.25)],
        num_list[int(len(num_list) * 0.75)],
    ]


def ft_std(*numbers: float) -> float:
    """Calculate the standard deviation of the given numbers."""
    return ft_var(*numbers) ** .5


def ft_var(*numbers: float) -> float:
    """Calculate the variance of the given numbers."""
    mean = ft_mean(*numbers)
    numbers = [(number - mean) ** 2 for number in numbers]
    return ft_mean(*numbers)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate and print various statistical measures based on input."""
    numbers: List[int] = []
    for i in args:
        try:
            numbers.append(int(i))
        except ValueError:
            print("Unable to parse '{}' to int.".format(i), file=sys.stderr)
            return

    for kw in kwargs.values():
        try:
            match kw:
                case "mean":
                    print("mean:", ft_mean(*numbers))

                case "median":
                    print("median:", ft_median(*numbers))

                case "quartile":
                    print("quartile:", ft_quartile(*numbers))

                case "std":
                    print("std:", ft_std(*numbers))

                case "var":
                    print("var:", ft_var(*numbers))
        except BaseException:
            print("ERROR", file=sys.stderr)


def main() -> None:
    """Execute the main program logic."""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
