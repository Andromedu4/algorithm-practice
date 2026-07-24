#Solution 1
def solution1(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

#Solution 2
def solution2(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum