"""Achiecing the same functionality of fucntions using idiomatic Python"""

__author__: str = "730812663"


def all(input: list[int], a: int) -> bool:
    if len(input) == 0:  # case where if length of the list is 0
        return False
    for elem in input:
        if elem != a:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")  # raising ValueError
    max_value = input[0]
    for elem in input:
        if elem > max_value:
            max_value = elem  # reassigning max value to a larger number in the list
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):  # case where length of lists are not equal
        return False
    for i in range(len(list_1)):  # checks same index values to see if they are equal
        if list_1[i] != list_2[i]:
            return False
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    for elem in list_2:
        list_1.append(elem)  # adds elements to list 1
