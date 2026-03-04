def discount(cost,d):
  ans= cost - (cost*(d/100))
  return ans

print('Enter the cost:')
x = int(input())
print('Enter the discount')
y = int(input())

print('Your final amount after discount is',discount(x,y))