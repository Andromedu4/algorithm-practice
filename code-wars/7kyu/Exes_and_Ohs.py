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

