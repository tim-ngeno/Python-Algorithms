#!/usr/bin/env python3
""" Two-pointer problem """


def two_pointer(lst, target):
    """ Solve a two-pointer problem """
    start = 0
    end = len(lst) - 1

    while start < end:
        left = lst[start]
        right = lst[end]

        sum = left + right

        if sum == target:
            return left, right

        elif sum < target:
            start += 1

        elif sum > target:
            end -= 1

    return 'No pair found'


arr = [1, 2, 4, 5, 6, 8, 9, 12]
target_sum = 11

print(two_pointer(arr, target_sum))
