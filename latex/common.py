"""
"""
from itertools import chain
from typing import Iterable

from minimization import to_bin


def split(iterable: Iterable, width=4):
    """ Generator yields iterable in parts.

    :param iterable: iterable to split
    :param width: length of each part
    """
    it = iter(iterable)
    while True:
        yield [next(it) for _ in range(width)]


if __name__ == '__main__':
    it = split(i for i in range(10))


def gen_gray(width=2, isbin=True):
    """ Generator yields successive Gray numbers.

    :param width: number of bits
    """
    for i in range(1 << width):
        gray = i ^ (i >> 1)
        bin_gray = to_bin(gray, width)
        yield (gray, bin_gray)[isbin]


def gen_fields(r_num: int, c_num=2):
    """ Generator yields order in table for flip-flops.

    :param r_num: number of rows
    :param c_num: number of cols
    """
    rows = gen_gray(r_num, False)
    cols = tuple(gen_gray(c_num, False))
    fac = 1 << c_num

    for row in rows:
        for col in cols:
            yield fac * row + col


def flatten(listOfLists):
    "Flatten one level of nesting"
    return tuple(chain.from_iterable(listOfLists))
