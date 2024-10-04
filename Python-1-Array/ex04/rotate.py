import sys
import numpy as np
from load_image import ft_load
from PIL import Image, UnidentifiedImageError


def my_transpose(array: list) -> list:
    """Transpose a square 2D array.
Returns a new transposed array."""
    size = len(array)
    new = np.zeros((size, size))

    for row_index, row in enumerate(array):
        for value_index, value in enumerate(row):
            new[value_index][row_index] = value
    return new


def main():
    """Main function to load an image, transpose a slice, and display it.
Handles various exceptions and exits with error messages if needed."""
    try:
        pixels = ft_load("animal.jpeg")
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(__file__ + ":", e.filename + ":", e.strerror,
              file=sys.stderr)
        sys.exit(1)
    except UnidentifiedImageError as e:
        print(__file__ + ":", e, file=sys.stderr)
        sys.exit(1)

    print(pixels)

    try:
        pixels = my_transpose(pixels[100:500, 450:850, 0])
        assert isinstance(pixels, np.ndarray), \
            "Transposed pixels should be a numpy array"
    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)
        sys.exit(1)
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
        sys.exit(1)

    print("New shape after slicing:", np.shape(pixels))
    print(pixels)

    img = Image.fromarray(pixels)
    img.show()


if __name__ == "__main__":
    main()
