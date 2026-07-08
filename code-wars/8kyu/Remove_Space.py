"""
Write a function that removes the spaces from the string, then return the resultant string.

Examples (Input -> Output):

"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"""

string = "8 j 8   mBliB8g  imjB8B8  jl"

def no_space(x):
    return x.replace(' ' ,'')

def no_space2(x):
    return "".join(x.split())

print(no_space2(string))

