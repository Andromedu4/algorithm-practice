"""
Write a function that removes the spaces from the string, then return the resultant string.

Examples (Input -> Output):
"""

string = "8 j 8   mBliB8g  imjB8B8  jl"

def no_space(x):
    return x.replace(' ' ,'')

def no_space2(x):
    return "".join(x.split())

print(no_space2(string))

