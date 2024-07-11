#!/usr/bin/env python3
"""Given two arrays, write a function that returns the intersection of
the two arrays. The intersection should contain unique elements only"""


def find_array_intersection(array1, array2):
    """Finds the intersection of 2 arrays and returns unique elements"""
    return list(set(i for i in array1 if i in array2))


array1 = [1, 2, 2, 3]
array2 = [2, 2, 4, 3]

arr3 = [1, 2, 3]
arr4 = [4, 5, 6]

print(f"Array 1: ", array1)
print(f"Array 2: ", array2)

print(find_array_intersection(array1, array2))


print(f"Array 3: ", arr3)
print(f"Array 4: ", arr4)
print(find_array_intersection(arr3, arr4))
