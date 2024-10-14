"""Mutating functions."""

__author__: str = "730812663"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(a: list[int], integer: int) -> None:
    a.append(integer)
    print(a)


def double(a: list[int]) -> None:
    index = 0
    while index < len(a):
        a[index] = a[index] * 2
        index = index + 1
    print(a)


double(list_2)
print(list_1)
print(list_2)
