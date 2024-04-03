#!/usr/bin/env python3
""" Finds the index of a value in an unordered list """
from typing import List


def find_index(lst: List, key: int) -> int:
    """
    Takes a list of integers and a key to find in the list

    Args:
        lst: (list): A list of integers
        key (int): A key to find in the list

    Returns:
        (int): The index of the element if it exists, or -1 otherwise
    """
    for i in range(len(lst)):
        if lst[i] == key:
            return i

    return -1


if __name__ == "__main__":
    number_to_search: int = 8
    numbers: List = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    for idx, i in enumerate(numbers):
        print(f'Index {idx} = {i}')
    x = find_index(numbers, number_to_search)
    print(f'Number {number_to_search} is at index {x}')
