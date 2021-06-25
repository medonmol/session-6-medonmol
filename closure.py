from functools import wraps

############################### 1
def check_docstring_len(fn):
    """
    Accepts a function and checks if the length of the 
    docstring is greater than 50
    """
    from inspect import getdoc

    limit = 50

    @wraps(fn)
    def inner():
        nonlocal limit
        fn_docstr = getdoc(fn)
        if fn_docstr is None:
            return False
        len_docstring = len(fn_docstr)
        if len_docstring > limit:
            print(f"the docstring for {fn.__name__} is greater than {limit}")
            return True
        else:
            print(f"the docstring for {fn.__name__} is lesser than {limit}")
            return False

    return inner


############################### 2


def get_next_fibonacci(fn):
    """
    Returns the next fibonacci number
    """
    ctr = 0

    @wraps(fn)
    def inner():
        nonlocal ctr
        val = fn(ctr)
        ctr += 1
        return val

    return inner


############################### 3
counters = {}


def counter(fn):
    """
    A simple counter that keeps track of how many times 
    a function has been run.
    """

    @wraps(fn)
    def inner(*args, **kwargs):
        global counters
        if fn.__name__ in counters:
            counters[fn.__name__] += 1
        else:
            counters[fn.__name__] = 1

        return f"{fn.__name__} has been called {counters[fn.__name__]} times"

    return inner


############################### 4


def counter_with_diff_dict(fn, counter_dict):
    """
    A simple counter that accepts a fn and a dict, 
    and stores the number of times the fn has been called
    in that dict

    """

    @wraps(fn)
    def inner(*args, **kwargs):
        if fn.__name__ in counter_dict:
            counter_dict[fn.__name__] += 1
        else:
            counter_dict[fn.__name__] = 1

        return counter_dict

    return inner
