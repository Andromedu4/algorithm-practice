#Solution 1
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result

#Solution 2
def rental_car_cost1(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30