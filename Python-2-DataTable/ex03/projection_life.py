from matplotlib import pyplot as plt
from load_csv import load


def main() -> None:
    """Load GDP and life expectancy data, then plot a scatter plot for 1900."""
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life_expectancy = load("life_expectancy_years.csv")

    if df_gdp is not None and df_life_expectancy is not None:
        plt.scatter(df_gdp["1900"].values, df_life_expectancy["1900"].values)
        plt.xscale("log")
        plt.xticks([300, 1_000, 10_000], ["300", "1k", "10k"])
        plt.title("1900")
        plt.xlabel("Life Expectancy")
        plt.ylabel("Gross Domestic Product")
        plt.show()


if __name__ == "__main__":
    main()
