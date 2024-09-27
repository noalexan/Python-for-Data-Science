import sys


def main():
    """
    This function is about to take str as argument, count
    every upper cases, lower cases, punctuations and digits
    """

    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) == 2:
        input = sys.argv[1]
    else:
        sys.stdout.write("Enter string: ")
        sys.stdout.flush()
        try:
            input = sys.stdin.readline()
        except UnicodeDecodeError:
            raise RuntimeError(
                "You enterred unicode characters. Please keep using utf-8.")

    upper_case_sum = len(''.join(filter(str.isupper, input)))
    lower_case_sum = len(''.join(filter(str.islower, input)))
    digits_sum = len(''.join(filter(str.isdigit, input)))
    spaces_sum = len(''.join(filter(str.isspace, input)))
    total = len(input)
    punctuation_sum = total - upper_case_sum - \
        lower_case_sum - digits_sum - spaces_sum

    print(f"""
  The text contains {total} characters:
    {upper_case_sum} upper letters
    {lower_case_sum} lower letters
    {punctuation_sum} punctuation marks
    {spaces_sum} spaces
    {digits_sum} digits
""")


if __name__ == "__main__":
    main()
