#!/usr/bin/env python3
""" Check that a string is a valid palindrome """


def valid_palindrome(text):
    """
    Checks that a string is a valid palindrome

    Args:
        text (str): String to be checked
    """
    # Convert to lowecase, remove non-alphanumeric characters
    text = ''.join(char.lower() for char in text if char.isalnum())

    # Initialize 2 pointers, at the start and at the end
    start = 0
    end = len(text) - 1

    while start < end:
        left = text[start]
        right = text[end]

        if left != right:
            return False
        start += 1
        end -= 1
    return True


print(valid_palindrome('ala'))
print('A man, a plan, a canal: Panama: ',
      valid_palindrome('A man, a plan, a canal: Panama'))
print('Was it a car or a cat I saw?: ',
      valid_palindrome('Was it a car or a cat I saw?'))
print('No lemon, no melon: ', valid_palindrome('No lemon, no melon'))
print('A Santa at NASA: ', valid_palindrome('A Santa at NASA'))
print('12321: ', valid_palindrome('12321'))
print('Hello World: ', valid_palindrome('Hello World'))
