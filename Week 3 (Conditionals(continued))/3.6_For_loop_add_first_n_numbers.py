# For loop to add first n numbers:
  # n=5, ans= 0+1+2+3+4
n = int(input('Enter a number:'))
ans = 0
for i in range(n):
  ans = ans + i
print('Sum of first n numbers is:',ans)