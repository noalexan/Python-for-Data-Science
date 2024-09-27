import sys

if len(sys.argv) > 1:
    assert len(sys.argv) == 2, 'more than one argument is provided'

    try:
        int(sys.argv[1]), 'argument is not an integer'
    except ValueError:
        raise AssertionError("argument is not an integer")

    print("I'm Odd." if int(sys.argv[1]) % 2 else "I'm Even.")
