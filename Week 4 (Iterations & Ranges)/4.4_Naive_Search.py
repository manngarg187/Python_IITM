# Shotcut which we have to use:  'in' statement
# searching a no. in a list:  - Just for Practice
import random
l = []
for i in range(100000):
  l.append(random.randint(1,1000000))

print(l)

n = 0
while(n>-1):
  print("Enter a number, type -1 to exit:")
  n = int(input())
  flag = 0
  for i in range(len(l)):
    if (n==l[i]):
      print('Hip Hip Hurray, element found')
      flag = 1
      break
  if flag==0:
    print('Element not found')