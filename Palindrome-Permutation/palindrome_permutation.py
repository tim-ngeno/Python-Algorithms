#!/usr/bin/env python3
"""Palindrome permutation problem"""


def can_form_palindrome_permutations(s):
    """Checks if a string s can perform a palindrome permutation"""

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False
    return True


print(can_form_palindrome_permutations("aab"))
print(can_form_palindrome_permutations("code"))
print(can_form_palindrome_permutations("aac"))
