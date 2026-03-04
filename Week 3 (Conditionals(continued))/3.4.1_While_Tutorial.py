# Find factorial of the given no.

num = int(input('Enter the number: '))
fact = 1
if(num<=0):
  print('Not Defined')
else:
  while(num>0):
    fact = fact*num
    num = num - 1

print(fact)