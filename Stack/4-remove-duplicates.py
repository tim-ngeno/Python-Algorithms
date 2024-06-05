#!/usr/bin/env python3
""" Remove adjacent duplicates in a string """

Stack = __import__('0-stack').Stack


def remove_duplicates(s: str) -> str:
    """
    Removes adjacent duplicates in a string

    Args:
        s(str): The input string
    """
    stack = Stack()
    for char in s:
        if stack and stack.peek() == char:
            stack.pop()
        else:
            stack.push(char)
    return ''.join(stack.get_stack())


s = "abbaca"
res = remove_duplicates(s)
print(res)
