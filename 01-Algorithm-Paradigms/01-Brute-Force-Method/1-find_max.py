#!/usr/bin/env python3
""" Finds the maximum element's index """
from typing import List


def find_max_index(lst: List) -> int:
    """
    Takes a list of integers and returns the index of the maximum
    element in the list

    Args:
        lst (list): A list of integers

    Returns:
        (int): The index of the max element, -1 if it doesn't exist
    """
    # Initialize index to 0
    max_index: int = -1

    # Set max value to least number
    max_val: int = -99999

    for x in range(len(lst)):
        if max_val < lst[x]:
            max_val = lst[x]
            max_index = x

    return max_index


if __name__ == "__main__":
    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

    x: int = find_max_index(nums)
    print(nums)
    print(f'Maximum number in the list is {nums[x]}, at index {x}')
