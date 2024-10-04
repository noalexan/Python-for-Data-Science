import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice the input list and print shapes before and after slicing.
Returns the sliced list."""
    assert type(family) is list, "family must be a list"
    new_family = family[slice(start, end)]
    print("My shape is :", np.shape(family))
    print("My new shape is :", np.shape(new_family))
    return new_family


def main():
    """Execute the main program logic.
Demonstrates the slice_me function with different slice parameters."""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
