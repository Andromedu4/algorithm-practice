def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

x = odd_or_even([0])
print(x)