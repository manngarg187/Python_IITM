# Find all prime numbers less than the entered no.

n = int(input('Enter a number:'))
if(n>2):             # We are not writing n>=2 because read the question properly.
  print(2,end = ' ')
for i in range(3,n):
  flag = False
  for j in range(2,i):
    if(i%j==0):
      flag = False
      break
    else:
      flag = True
  if(flag):
    print(i,end=' ')

'''Method 2 -- I solved it this way! there is no need to consider '2' as question is saying prime no. less than the input no. so if we input 2 then there is no prime no. which is less than 2
n = int(input())
for i in range(2,n,1):
  x = True
  for j in range(2,i,1):
    if i%j == 0:
      x = False
  if x:
    print(i, end = " ")
'''