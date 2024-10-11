def callLimit(limit: int):
    """Decorator to limit function calls to a specified number."""
    count = 0

    def callLimiter(function):
        """Inner decorator function to wrap the original function."""
        def limit_function(*args: any, **kwargs: any):
            """Wrapped function that checks and limits the call count."""
            nonlocal count

            if count >= limit:
                return print(f"Error: {function} call too many times")

            count += 1

            return function(*args, **kwargs)

        return limit_function

    return callLimiter


def main():
    """Main function to demonstrate the usage of callLimit decorator."""
    @callLimit(3)
    def f():
        """Function f, limited to 3 calls."""
        print("f()")

    @callLimit(1)
    def g():
        """Function g, limited to 1 call."""
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
