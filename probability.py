import math
def combinations(n,k):
  return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))


print (combinations(52,5),"-",combinations(4,1),"*",combinations(52,3), "/" , combinations(52,5))
