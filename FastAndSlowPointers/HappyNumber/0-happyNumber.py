#!/usr/bin/env python3
""" Happy number algorithm """


def sum_of_squares(n):
    """
    Calculates the sum of squares of the digits of a number

    Args:
        n(int): Input integer
    """
    running_total = 0
    while n > 0:
        digit = n % 10
        running_total += digit ** 2
        n //= 10
    return running_total


def is_happy(num):
    """
    Checks if a number `num` is a happy number

    Args:
        num(int): Input number to check
    """
    seen = set()

    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    return num == 1


num = 19
if is_happy(num):
    print(f'{num} is a Happy number')
else:
    print(f'{num} is not a happy number')
