import sys
import numpy as np
from load_image import ft_load
from PIL import Image, UnidentifiedImageError


def ft_invert(array) -> np.array:
    """
    Invert the colors of the input image array and display the result.
    """
    copy = 255 - array[:, :, :]
    img = Image.fromarray(copy)
    img.show()
    return copy


def ft_red(array) -> np.array:
    """
    Isolate the red channel of the input image array and display the result.
    """
    copy = array.copy()
    copy[:, :, 1] = copy[:, :, 2] = 0
    img = Image.fromarray(copy)
    img.show()
    return copy


def ft_green(array) -> np.array:
    """
    Isolate the green channel of the input image array and display the result.
    """
    copy = array.copy()
    copy[:, :, 0] = copy[:, :, 2] = 0
    img = Image.fromarray(copy)
    img.show()
    return copy


def ft_blue(array) -> np.array:
    """
    Isolate the blue channel of the input image array and display the result.
    """
    copy = array.copy()
    copy[:, :, 0] = copy[:, :, 1] = 0
    img = Image.fromarray(copy)
    img.show()
    return copy


def ft_grey(array) -> np.array:
    """
    Convert the input image array to grayscale and display the result.
    """
    copy = array.mean(axis=2)
    img = Image.fromarray(copy)
    img.show()
    return copy


def main():
    """
    Load an image, display its pixels, and apply various image transformations.
    """
    try:
        pixels = ft_load("landscape.jpg")
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(__file__ + ":", e.filename + ":", e.strerror, file=sys.stderr)
        sys.exit(1)
    except UnidentifiedImageError as e:
        print(__file__ + ":", e, file=sys.stderr)
        sys.exit(1)

    print(pixels)

    ft_invert(pixels)
    ft_red(pixels)
    ft_green(pixels)
    ft_blue(pixels)
    ft_grey(pixels)


if __name__ == "__main__":
    main()
