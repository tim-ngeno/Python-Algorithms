# Palindrome Permutation

A palindrome permutation is a permutation (rearrangement) of the characters in a string that forms a palindrome. A palindrome is a string that reads the same forwards and backwards.

## Key properties of palindrome permutation
- Even Character Counts: For a string to have a palindromic permutation, every character in the string must appear an even number of times, except possibly one character that can appear an odd number of times (for strings with an odd length).

- At Most One Odd Count: If the length of the string is even, then all characters must appear an even number of times. If the length is odd, then at most one character can appear an odd number of times.

To determine if a string can form a palindrome permutation, you can follow these steps:
Count the frequency of each character in the string.
Check if at most one character has an odd frequency. If more than one character has an odd frequency, then a palindrome permutation is not possible.
If at most one character has an odd frequency, then the string can form a palindrome permutation.
For example, the string "aab" can form a palindrome permutation ("aba"), because 'a' appears twice (even) and 'b' appears once (odd). However, the string "code" cannot form a palindrome permutation, because 'c', 'o', 'd', and 'e' all appear an odd number of times.
The time complexity of checking if a string can form a palindrome permutation is O(n), where n is the length of the string, since we need to count the frequency of each character.
