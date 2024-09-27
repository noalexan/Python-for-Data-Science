import sys

from ft_filter import ft_filter


assert len(sys.argv) == 3, "the arguments are bad"
assert sys.argv[2].isdigit(), "the arguments are bad"

print([str for str in ft_filter(
    lambda str: len(str) > int(sys.argv[2]), sys.argv[1].split())])
