import utils
import closure
from random import randint
import pytest


def test_check_docstring_len_more_than_50():
    len_docstring_true = closure.check_docstring_len(utils.test_fn_docstring)

    assert len_docstring_true() == True


def test_check_docstring_len_no_docstring():
    len_docstring_none = closure.check_docstring_len(lambda x: x ** 2)
    assert len_docstring_none() == False


def test_check_docstring_len_less_than_50():
    len_docstring_false = closure.check_docstring_len(utils.add)
    assert len_docstring_false() == False


def test_check_docstring_non_function():
    len_docstring_non_function = closure.check_docstring_len(420)
    assert len_docstring_non_function() == False


def test_get_next_fibonacci():
    next_fibonacci = closure.get_next_fibonacci(utils.get_fib)
    fib_10 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(10):
        assert next_fibonacci() == fib_10[i]


def test_get_next_fibonacci0():
    fib = closure.get_next_fibonacci(utils.get_fib)
    assert fib() == 1


def test_count_fn1():
    count_add = closure.counter(utils.add)
    for _ in range(10):
        count_add(1, 2, 3, 4)
    assert closure.counters.get("add") == 10


def test_count_fn2():
    count_mult = closure.counter(utils.mult)
    for _ in range(10):
        count_mult(2, 1, 2)
    assert closure.counters.get("mult") == 10
    assert closure.counters.get("add") == 10


def test_count_fn3():
    count_div = closure.counter(utils.div)
    for _ in range(100):
        count_div(100 / 2)
    assert closure.counters.get("div") == 100
    assert closure.counters.get("add") == 10


def test_count_fn4():
    count_mult = closure.counter(utils.mult)
    for _ in range(10):
        count_mult(2, 1, 2)
    count_add = closure.counter(utils.add)
    for _ in range(10):
        count_add(2, 1, 2)
    assert closure.counters.get("mult") == 20
    assert closure.counters.get("add") == 20


def test_count_fn5():
    count_div = closure.counter(utils.div)
    for _ in range(30):
        count_div(10 / 2)
    count_mult = closure.counter(utils.mult)
    for _ in range(30):
        count_mult(10 / 2)
    assert closure.counters.get("div") == 130
    assert closure.counters.get("mult") == 50


def test_count_fn6():
    count_mult = closure.counter(utils.mult)
    for _ in range(10):
        count_mult(2, 1, 2)
    assert closure.counters.get("mult") == 60


def test_counter_with_diff_dict1():
    dict_add = {}

    counter_add = closure.counter_with_diff_dict(utils.add, dict_add)

    rand_add = randint(1, 100)

    for _ in range(rand_add):
        counter_add()

    assert dict_add.get("add") == rand_add


def test_counter_with_diff_dict2():
    dict_add = {}
    dict_mult = {}

    counter_add = closure.counter_with_diff_dict(utils.add, dict_add)
    counter_mult = closure.counter_with_diff_dict(utils.mult, dict_mult)

    rand_add = randint(1, 100)
    rand_mult = randint(1, 100)

    for _ in range(rand_add):
        counter_add()
    for _ in range(rand_mult):
        counter_mult()

    assert dict_add.get("add") == rand_add
    assert dict_mult.get("mult") == rand_mult


def test_counter_with_diff_dict3():
    dict_add = {}
    dict_mult_div = {}

    counter_add = closure.counter_with_diff_dict(utils.add, dict_add)
    counter_mult = closure.counter_with_diff_dict(utils.mult, dict_mult_div)
    counter_div = closure.counter_with_diff_dict(utils.div, dict_mult_div)

    rand_add = randint(1, 100)
    rand_mult = randint(1, 100)
    rand_div = randint(1, 100)

    for _ in range(rand_add):
        counter_add()
    for _ in range(rand_mult):
        counter_mult()
    for _ in range(rand_div):
        counter_div()

    assert dict_add.get("add") == rand_add
    assert dict_mult_div.get("mult") == rand_mult
    assert dict_mult_div.get("div") == rand_div


def test_counter_with_diff_dict4():
    dict_add = {}
    dict_mult = {}
    dict_div = {}

    counter_add = closure.counter_with_diff_dict(utils.add, dict_add)
    counter_mult = closure.counter_with_diff_dict(utils.mult, dict_mult)
    counter_div = closure.counter_with_diff_dict(utils.div, dict_div)

    rand_add = randint(1, 100)
    rand_mult = randint(1, 100)
    rand_div = randint(1, 100)

    for _ in range(rand_add):
        counter_add()
    for _ in range(rand_mult):
        counter_mult()
    for _ in range(rand_div):
        counter_div()

    assert dict_add.get("add") == rand_add
    assert dict_mult.get("mult") == rand_mult
    assert dict_div.get("div") == rand_div


def test_counter_with_list5():
    dict_add = []

    with pytest.raises(utils.CustomCounterException):
        _ = closure.counter_with_diff_dict(utils.add, dict_add)


def test_counter_with_invalid_function6():
    dict_add = {}

    with pytest.raises(utils.NoFunctionException):
        _ = closure.counter_with_diff_dict(dict_add, dict_add)
