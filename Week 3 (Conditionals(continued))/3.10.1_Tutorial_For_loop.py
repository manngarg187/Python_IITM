# Find factorial of the given no. (for loop) #Preferred

num = int(input('Enter the number: '))
fact = 1
if(num<=0):
  print('Not Defined')
else:
  for i in range(num,1,-1):   # when you know the range then prefer for loop over while loop
    fact = fact*i

print(fact)