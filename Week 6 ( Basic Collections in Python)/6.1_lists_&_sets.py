# CONCLUSION: To check something is there or not in a big database, then we use a SET. If we want to refer to element in the dataset then we use a LIST

# Sir, took an example of a Car and a Bus. 
# Car & Bus have there own pros and cons.
# Car has a good Mileage but Bus don't have good mileage
# Car can only carry 5 people but Bus has capacity to carry more than 50 people.
# Car is more mobile than bus as car can easily travel on narrow roads too but bus can't


       # Learning:  Trade off : If you want to Gain something in life, you may have to give up on some other things in life.  

l = list(range(10))
print(l)
l.append('mann')
l.append('2.70')
print(l)
print(3 in l)                 # by 'in' commend we can directly search in a list
print('mann' in l)
print(-1 in l)
l = list(range(100000))
print(l[0])
print(l[len(l)-1])
print(1 in l)       # It's output comes very fast as it is able to find '1' in the beginning of the list
print('mann' in l)  # It took some time to give 'false' as output as 'mann' is not there in the updated l, it is taking time as 
                    # is has to go from no. 1 element till the end to find it, that 'mann' is there in list or not
print('............................................')
x = [1,2,5,9,2,9,1,0]    # List    
y = {1,9,2,3,7,1}        # Set
print(type(x))
print(type(y))
print(x)      # output: [1, 2, 5, 9, 2, 9, 1, 0]
print(y)      # output: {1, 2, 3, 7, 9} - Here in this output, automatically repetation of '1' is removed and data is arranged in accending order. So in curly brackets, the entity becomes set, and it automatically removes repetation within it.

# Remember: Repetation are not allowed in a set

print(2 in y)    # Note: So the in operator works also in set
print(-1 in y)

print('...................................')
l = list(range(100000))
s = set(range(100000))  
# set(range(100000)) will going to take more time to form as compared to list(range(100000))
print(1 in l)
print(-1 in l)
print(1 in s)
print(-1 in s)
# 'in' operator will take more time to search -1 in list l as compared to set s

# Note: Searching in Set is easy as compared to searching in List

import sys

l = []
l1 = [0]
l2 = [0,1]
print(sys.getsizeof(l))  # 56 bits
# sys.getsizeof(l) tells me what is the size of l in the memory of your computor
print(sys.getsizeof(l1))  # 64 bits
print(sys.getsizeof(l2))  # 72 bits
x = list(range(100))
s = set(range(100))
print(sys.getsizeof(x))   # 856 bits
print(sys.getsizeof(s))   # 8408 bits (It takes almost 10 times more space as compared to the size of list)

# We can't call a particular element by it's position in a set : That's why print(s[1]) will going to through an error
# Note: In a set we can only tell that is there a element present in it or not, but we can't tell that it is first element or second element...

print('..........................................')

z = {'mann','meet','ansh','kushal'}
z.add('agrim')      # z.add() command is used to include some element in the set
print(z) 

# CONCLUSION: To check something is there or not in a big database, then we use a SET. If we want to refer to element in the dataset then we use a LIST