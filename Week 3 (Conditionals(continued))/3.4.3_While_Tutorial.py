# Reverse the digits in the given no.

num = int(input('Enter the number: '))
absNum = abs(num)
rev = absNum%10
absNum = absNum//10
while(absNum > 0):
  r = absNum % 10
  absNum = absNum//10
  rev = rev*10 + r
if(num >= 0):
  print(rev)
else:
  print(rev-2*rev) 