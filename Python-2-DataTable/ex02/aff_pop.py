import sys
from typing import List
from matplotlib import pyplot as plt
from pandas import DataFrame
from load_csv import load


def csv_query(data_frame: DataFrame,
              column_name: str,
              value: any) -> DataFrame:
    """Filter all rows where the specified column matches the given value."""
    return data_frame[data_frame[column_name] == value]


def parse_number(value: str) -> float:
    """Convert a string with a suffix (K, M, B) to a float."""

    suffixes = {
        "K": 1_000,
        "M": 1_000_000,
        "B": 1_000_000_000
    }

    if value[-1].upper() in suffixes:
        return float(value[:-1]) * suffixes[value[-1].upper()]

    return float(value)


def add_country_population(data_frame: DataFrame, country_name: str) -> None:
    """Plot population over the years for a specified country."""
    years = [year for year in data_frame.columns[1:]
             if year.isdigit() and 1800 <= int(year) <= 2050]
    query = csv_query(data_frame, "country", country_name)

    if query.empty:
        print(f"No entry for '{country_name}'", file=sys.stderr)
        return

    rows = query.values
    country_data = [parse_number(num) for num in rows[0, 1:(len(years) + 1)]]

    plt.plot(years, country_data, label=country_name)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks(years[::40])
    plt.yticks(
        [20_000_000, 40_000_000, 60_000_000],
        ["20M", "40M", "60M"]
    )


def countries_population(
        data_frame: DataFrame,
        countries_name: List[str]) -> None:
    """Plot several countries population and display."""
    for country_name in countries_name:
        add_country_population(data_frame, country_name)

    plt.legend(loc="lower right")
    plt.show()


def main() -> None:
    """Load data and plot populations for given countries."""
    data_frame = load("population_total.csv")

    if data_frame is not None:
        countries_population(data_frame, ["France", "Belgium"])


if __name__ == "__main__":
    main()
