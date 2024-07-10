#!/usr/bin/env python3
"""Given a string, write a function that returns the first non-repeating
character in the string. If all the characters are repeating, return None"""


def find_non_repeating_char(string):
    """Takes an input string and returns the character in the string
    that occurs only once

    Args:
        string (str): The input string

    Returns:
        str: The character that occurs only once or None
    """
    hash_map = {}
    for char in string:
        hash_map[char] = hash_map.get(char, 0) + 1

    for char, freq in hash_map.items():
        if freq == 1:
            return char
    return None


string1 = "aabbcc"
string2 = "aabbc"

print(find_non_repeating_char(string1))
print(find_non_repeating_char(string2))
