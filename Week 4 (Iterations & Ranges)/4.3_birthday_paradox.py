# Birthday Paradox
# Whatever we are about to do here is called "Scientific Simulations"
# 

import random

l = []
# create an empty list

for i in range(30):
  l.append(random.randint(1,365))
  #append random numbers between 1 to 365
  #append 30 of them
l.sort()
print(l)
i = 0
flag = 0   #denotes that there is no repetition
while i < (len(l) - 1):
  if l[i] == l[i+1]:
    print('Repetition',l[i],l[i+1])
    flag = 1
    break
  i = i+1
if flag == 0:
  print('NO REPETITION')

# when I ran this experiment so many times, it proved that birthday pardox was true.

'''Sir:

Let us run the experiment.  I said the word experiment,  
what I mean by that? You need not go to the roads  or go to a classroom and then run this experiment.  
You see, you noted that in the computational  thinking course, the professors were using the  
cards to show you that the repetition  happens. Is that really true?  
You can come here and run an experiment on  your computer, repeat the experiment many  
times and then say that this is indeed  true. When you repeat the experiment,  
this paradox called the birthday paradox, paradox  is something that is tough to believe but is true,  
indeed is visible here in this experiment where  you pick numbers from 1 to 365, uniformly it  
random a few times, put them into an array, sort  it so that it is easy for you to see repetition,  
you will say that there are repetitions. 

I hope you enjoyed the piece of code here,  
what we did just now is called simulation in  the language of science and it is called the  
scientific simulation. Many many researchers do  this and they write research papers based on this.  
You can in fact simulate how Covid disease  spreads just on your Python compiler.  
You can simulate how the stock market  works just on your Python editor.  
So, this was a good introduction to what  you mean by a simulator, but then what  
interest us the most right now is confidence  to write a piece of code. We just now wrote  
a nice piece of code which told us indeed  birthday paradox is true. So, from now onwards,  
whenever someone says something, if you think that  is numerically possible to simulate, you should  
quickly switch on your computer, write a piece  of code and then analyse the output of the code.'''