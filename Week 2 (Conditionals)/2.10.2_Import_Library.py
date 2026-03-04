# Let us simulate a coin toss
import random

a = random.random() #random.random picks a no. b/w 0 & 1
print(a)

if(a>0.5):
  print('Heads')
else:
  print('Tails')