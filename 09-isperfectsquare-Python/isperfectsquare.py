# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

import math
def isperfectsquare(n):
  #n=int(n)
  if isinstance(n, int) and n>=0:
    return n == (math.sqrt(n)**2)
  elif isinstance(n, int) and  n<=0:
    return False
  elif isinstance(n, float):
    return False
  elif n.isdigit():
    n=int(n)
    return n == (math.sqrt(n)**2)
  else:
    return False