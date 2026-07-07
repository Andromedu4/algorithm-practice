
array = [1,5,3]

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

print(find_average(array))
