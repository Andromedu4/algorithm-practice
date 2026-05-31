# built in function
def convert_to_binary(a,b):
    sum = a + b
    return bin(sum)[2:]

print(convert_to_binary(2,4))

""" Manual solution
# find_power - index
def find_power(num):
    n = 0

    while 2**n <= num:
        n += 1

    return n-1

# convert_to_binary

def conver_to_binary(a,b):
    sum = a + b
    number = 0

    while sum != 0:
        index = find_power(sum)
        number += 10**index
        sum -= 2**index

    return number

print(conver_to_binary(2,6))
"""