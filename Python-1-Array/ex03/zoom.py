import sys
import numpy as np
from load_image import ft_load
from PIL import Image, UnidentifiedImageError


def main():
    """Load an image, slice it, and display the result.
Handles exceptions for file loading and image identification errors."""
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

    pixels = pixels[slice(100, 500), slice(450, 850)]

    print("New shape after slicing:", np.shape(pixels))
    print(pixels)

    img = Image.fromarray(pixels)
    img.show()


if __name__ == "__main__":
    main()
