#!/usr/bin/env python3
"""Given a string, write a function that returns the frequency of each
character in the string. The function should return a dictionary/hash
map where the keys are the characters and the values are their
respective frequencies."""


def character_frequency(string):
    """Takes an input string and returns a hash map containing the
    charcter as keys and the frequency of the words as the value(s)

    Args:
        string (str): The input string
    """
    # Create a hash map
    result = {}

    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


string = "hello world"

print(character_frequency(string))
