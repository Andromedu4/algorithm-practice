"""
In this Kata we are passing a number (n) into a function.
Your code will determine if the number passed is even (or not).
The function needs to return either a true or false.
Numbers may be positive or negative, integers or floats.
"""

#Solution 1
def is_even(n):
    return n%2 == 0

#Solution 2
def is_even2(n):
    return not n % 2