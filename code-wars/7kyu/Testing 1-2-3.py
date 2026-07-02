"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.
"""
number = [2,4]
# Solution 1
def number1(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
#Solution 2
def number2(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
#Solution 3
def number3(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]
print(number1(number))