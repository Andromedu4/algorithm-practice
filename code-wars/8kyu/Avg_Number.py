"""
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
"""

array = [1,5,3]

def find_average(array):
    return sum(array) / len(array) if array else 0

print(find_average(array))