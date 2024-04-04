#!/usr/bin/env python3
""" Balanced brackets problem """

Stack = __import__('0-stack').Stack


def balanced_brackets(bracket_string: str):
    """

    """
    s = Stack()
    is_balanced: bool = True
    index = 0

    while index < len(bracket_string) and is_balanced:
        bracket = bracket_string[index]
        if bracket in '({[':
            s.push(bracket)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, bracket):
                    is_balanced = False
                    break
        index += 1

    return s.is_empty() and is_balanced


def is_match(p1, p2):
    """
    Compares the opening and closing types of brackets and returns
    true if they match, False otherwise
    """
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(balanced_brackets("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(balanced_brackets("[][]]]"))

print("String : [][] Balanced or not?")
print(balanced_brackets("[][]"))
