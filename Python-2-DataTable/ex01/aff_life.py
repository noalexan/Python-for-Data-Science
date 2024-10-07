import sys
from matplotlib import pyplot as plt
from pandas import DataFrame
from load_csv import load


def csv_query(data_frame: DataFrame,
              column_name: str,
              value: any) -> DataFrame:
    """Filter all rows where the specified column matches the given value."""
    return data_frame[data_frame[column_name] == value]


def country_life_expectancy(data_frame: DataFrame, country_name: str) -> None:
    """Plot life expectancy over the years for a specified country."""
    years = data_frame.columns[1:]
    query = csv_query(data_frame, "country", country_name)

    if query.empty:
        print(f"No entry for '{country_name}'", file=sys.stderr)
        return

    rows = query.values
    country_data = rows[0, 1:]

    plt.plot(years, country_data)
    plt.title(f"{country_name} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.xticks(years[::40])
    plt.show()


def main() -> None:
    """Load data and plot life expectancy for France."""
    data_frame = load("life_expectancy_years.csv")

    if data_frame is not None:
        country_life_expectancy(
            data_frame,
            sys.argv[1] if len(sys.argv) > 1 else "France")


if __name__ == "__main__":
    main()
