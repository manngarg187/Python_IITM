# Let us simulate a sum of 2 dice (six faced)
import random
dice1 = (random.randrange(1,7)) # randrange doesn't include rightmost part of entered range, here that is '7'
dice2 = (random.randrange(1,7))
print(dice1)
print(dice2)
total = dice1 + dice2
print('Your pair of dice is',total)