"""Summing the elements of a list using different loops"""

__author__: str = "730812663"


def w_sum(vals: list[float]) -> float:
    sum = 0.0
    index = 0
    while index < len(vals):
        sum = sum + vals[index]
        index = index + 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    for idx in range(0, len(vals)):
        sum = sum + idx
    return sum
