# Anagram Grouping

This Python program groups anagrams together from a given list of words.

## Problem Statement

Given a list of words, the goal is to group anagrams together. Anagrams are words that have the same characters but in a different order.

For example, given the list `["eat", "tea", "tan", "ate", "nat", "bat"]`, the output should be:

```
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

## Solution

The program uses a dictionary (hash map) to efficiently group anagrams together. Here's how it works:

1. Iterate through each word in the input list
2. For each word, sort its characters alphabetically to get a "key" 
3. If the key already exists in the dictionary, append the original word to its value list
4. If the key doesn't exist yet, create a new key-value pair with the key being the sorted word and the value being a list containing the original word
5. After processing all words, convert the dictionary values to a list and return it

The program will output the grouped anagrams.

## Time and Space Complexity

- Time complexity: O(N * M * log M), where N is the number of words and M is the average length of each word.
- Space complexity: O(N * M) to store the dictionary.
