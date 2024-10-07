import sys
from pandas import DataFrame, read_csv
from pandas.errors import ParserError


def load(path: str) -> DataFrame | None:
    """
    Load a CSV file into a pandas DataFrame.
    Returns None if an error occurs during loading.
    """
    try:
        data_file = read_csv(path)
    except (ParserError, FileNotFoundError,
            IsADirectoryError, PermissionError) as e:
        print((path + ": " if type(e) is ParserError else "") + str(e),
              file=sys.stderr)
        return None
    print("Loading dataset of dimensions:", data_file.shape)
    return data_file


def main():
    """
    Main function to load and print a CSV file.
    Exits with an error if no file path is provided.
    """
    if len(sys.argv) <= 1:
        print(__file__ + ":", "<path to csv>", file=sys.stderr)
        sys.exit(1)

    print(load(sys.argv[1]))


if __name__ == "__main__":
    main()
