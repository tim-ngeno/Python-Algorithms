#!/usr/bin/env python3
""" Convert an integer to binary """

Stack = __import__('0-stack').Stack


def int_to_binary(num):
    """
    Converts an integer num to its equivalent binary number
    """
    if num == 0:
        return 0

    stack = Stack()
    while num > 0:
        stack.push((num % 2))
        num //= 2

    # get the bits in reverse order
    bits = stack.get_stack()[::-1]
    print(bits)
    bits_as_str = ''.join(str(i) for i in bits)
    return bits_as_str


print(int_to_binary(242))
print(int_to_binary(142))
print(int_to_binary(24))
print(int_to_binary(42))
print(int_to_binary(56))
