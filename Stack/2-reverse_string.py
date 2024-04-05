#!/usr/bin/env python3
""" Reversing a string using a stack """

Stack = __import__('0-stack').Stack


def reverse_string(stack, input_string: str) -> str:
    """
    Reverse a string using the stack algorithm

    Args:
        stack (Stack): An instance of the stack class
        input_string (str): The input string to be reversed
    """
    rev_str = ""
    for i in input_string:
        stack.push(i)
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()
input_string = '!dlrow ,olleH'
print(reverse_string(stack, input_string))
