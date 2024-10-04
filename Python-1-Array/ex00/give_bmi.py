def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate BMI for each pair of height and weight.
Returns a list of BMI values."""
    assert len(height) == len(weight), \
        "Height and weight lists must be of the same length."
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI value exceeds the given limit.
Returns a list of boolean values."""
    return [x > limit for x in bmi]


def main():
    """Execute the main program logic.
Calculates BMI and applies a limit check."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
