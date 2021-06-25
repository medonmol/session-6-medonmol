from functools import reduce, lru_cache


@lru_cache()
def calculate_fib(n):
    """
    Calculates the nth fibonacci number

    """
    if n < 2:
        return 1
    else:
        return calculate_fib(n - 1) + calculate_fib(n - 2)


def get_fib(n):
    """
    wrapper around the calculate_fib function
    """
    return calculate_fib(n)


def add(*args):
    """
    Add integers
    """

    return reduce(lambda x, y: x + y, args)


def mult(*args):
    """
    Multiply numbers
    """
    return reduce(lambda x, y: x * y, args)


def div(a, b):
    """
    divide 2 numbers
    """
    return a / b


def test_fn_docstring():
    """
    Test function for the check_docstring_len function.
    Input: None

    Output: Nothing really

    """
    return


class CustomCounterException(Exception):
    """
    Custom Exception to handle invalid data structure in Counters
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class NoFunctionException(Exception):
    """
    Custom Exception calss to handle invalid function parameter
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message
