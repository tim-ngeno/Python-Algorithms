#!/usr/bin/env python3
""" Creating a Hash Map """


class HashMap:
    def __init__(self, size=10):
        """
        Initializes a HashMap object with a specified size and creates
        an array of empty lists

        Args:
            size(int): Size of the hash map. Default value is 10.
        """
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Calculates the index for a given key using the hash() function.

        Args:
            key: The input key whose index is to be calculated.

        Returns:
            int: The index corresponding with the key
        """
        return hash(key) % self.size

    def put(self, key, value):
        """
        Calculates the index for the key and checks if it exists, then
        updates its value, or appends the key-value pair if it doesn't

        Args:
            key: The key to be added or updated
            value: The value associated with the array
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        """
        Retrieves the value associated with a given key.

        Args:
            key: The key whose value is to be retrieved

        Returns:
            The value associated with the key, or None if the key
            doesn't exist
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """
        Removes the key-value pair associated with a given key

        Args:
            key: the key to be removed

        Returns:
            bool: True if the key was found and removed, False otherwise
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


hash_map = HashMap()

hash_map.put('apple', 50)
hash_map.put('banana', 30)
hash_map.put('orange', 20)

# Retrieve values
print(hash_map.get('apple'))
print(hash_map.get('banana'))
print(hash_map.get('orange'))
print(hash_map.get('grape'))

# Remove a key
print('Removing key "banana"')
hash_map.remove('banana')
print(hash_map.get('banana'))
