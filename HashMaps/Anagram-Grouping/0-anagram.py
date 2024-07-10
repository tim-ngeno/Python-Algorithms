#!/usr/bin/env python3
"""Grouping anagrams using a hash map"""


def group_anagrams(words):
    """Groups anagrams together and returns a list of the grouped
    words

    Args:
        words (list): A list of words(strings) to be grouped
    """
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)

    print(result)
