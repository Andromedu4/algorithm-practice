"""
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

"""
#Solution 1
def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result

#Solution 2
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30