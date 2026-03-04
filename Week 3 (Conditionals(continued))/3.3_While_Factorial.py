 # finding factorial of a no.
print('Enter a number:')
n=int(input())

# 5! = 1*2*3*4*5

answer = 1
i = 1
while(i<=n):
  answer = answer*i
  i = i+1
print(answer)

'''
answer = 1
i = 1
n = 5
answer = 1
i = 2
answer = 2
i = 3
answer = 6
i = 4
answer = 24
i = 5
answer = 120
i = 6 (Her this don't satisfy our while loop so it will exit from while loop
'''