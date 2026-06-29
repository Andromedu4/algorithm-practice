"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
"""

#Solution 1
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
#Solution 2
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
#Solution 3
def xo(s):

  exes = 0
  ohs = 0

  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1

  return exes == ohs

