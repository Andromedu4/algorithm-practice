

string = "8 j 8   mBliB8g  imjB8B8  jl"

def no_space(x):
    return x.replace(' ' ,'')

def no_space2(x):
    return "".join(x.split())

print(no_space2(string))

