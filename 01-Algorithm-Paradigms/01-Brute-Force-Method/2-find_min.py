#!/usr/bin/env python3
""" Find the index of the min element """

from typing import List


def find_min_index(lst: List) -> int:
    """
    Takes a list of integers and returns the index of the minimum
    element from the list

    Args:
        lst (list): A list of integers

    Returns:
        The index of the min element, -1 otherwise
    """

    min_index: int = -1
    min_val: int = 99999

    for i in range(len(lst)):
        if min_val > lst[i]:
            min_val = lst[i]
            min_index = i

    return min_index


if __name__ == "__main__":
    nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]
    x = find_min_index(nums)

    print(nums)
    print(f'Minimum number in the list is: {nums[x]}, at index {x}')
