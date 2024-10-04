import sys
import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> list:
    """Load an image from the given path and convert it to a numpy array.
Print the shape of the image and return the pixel array."""
    with Image.open(path) as img:
        pixels = np.asarray(img)
        print("The shape of image is", np.shape(pixels))
    return pixels


def main():
    """Execute the main program logic. Load and display image
data from the path provided as a command-line argument."""
    if len(sys.argv) <= 1:
        print(__file__ + ":", "<path to image>", file=sys.stderr)
        sys.exit(1)

    try:
        print(ft_load(sys.argv[1]))
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(__file__ + ":", e.filename + ":", e.strerror,
              file=sys.stderr)
    except UnidentifiedImageError as e:
        print(__file__ + ":", e, file=sys.stderr)


if __name__ == "__main__":
    main()
