# recursion in python

def sum(n):
  if n==1:
    return 1
  else:
    return (sum(n-1) + n)

print(sum(8))

# Note: Python let's you call the same function within the function

# coumpute the compound interest by assuming the interest to be 10%
def compound(p,n):
  if n==1:
    return p*1.1
  else:
    return (compound(p,n-1))*1.1

print(compound(10000,10))

# Compute the factorial by recursion

def fact(n):
  if n==1:
    return 1
  else:
    return fact(n-1)*n

print(fact(6))