"""Homework task 03."""
from functools import reduce
import itertools


def squares(a):
    """Generator. Yields a^2."""
    for it in a:
        yield int(it) ** 2


def repeatntimes(elems, n):
    """Generator. Yields from elems n times."""
    it = itertools.tee(elems, n)
    for i in it:
        yield from i


def evens(x):
    """Generator. Yilds even numbers from x."""
    if x % 2:
        x += 1
    while True:
        yield x
        x += 2


def digitsumdiv(p):
    """Generator.

    Yields numbers which sum of digits is divisible by p in ascending order
    """
    for i in itertools.count(1):
        if not sum(map(int, str(i))) % p:
            yield i


def extractnumbers(s):
    """Generator.

    Yields digits from arbitrary string.
    """
    return filter(lambda x: x.isdigit(), s)


def changecase(s):
    """Generator.

    Yield all symbols from string s.
    If symbol is english letter change its case before yielding.
    """
    return map(lambda x: x.swapcase() if x.isalpha() else x, s)


def productif(elems, conds):
    """Function.

    Return product of elements from elems
    such that corresponding element of conds is True.
    Length of conds may be less than length of elems.
    """
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] else 1,
                  zip(elems, conds)), 1)
