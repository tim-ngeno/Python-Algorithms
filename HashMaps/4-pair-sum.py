#!/usr/bin/env python3
"""Pair Sum
Given an array of integers and a target sum, write a function that
returns a pair of elements from the array that add up to the target
sum. If no such pair exists, return None."""


def pair_sum(arr, target):
    """
    Takes an array and a target sum and finds a pair of elements that
    add up to the target sum from the input array

    Args:
        arr (list): A list of integers
        target (int): The target sum
    """
    complements = set()

    for num in arr:
        complement = target - num
        if complement in complements:
            return (num, complement)
        complements.add(num)
    return None


print(pair_sum([1, 2, 3, 4, 5], 7))  # Output: (2, 5)
print(pair_sum([1, 2, 3, 4, 5], 2))  # Output: None
print(pair_sum([3, 5, 2, 8, 1, 4], 7))  # Output: (2, 5)
