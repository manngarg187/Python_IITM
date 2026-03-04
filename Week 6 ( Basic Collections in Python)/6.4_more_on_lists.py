# Concept 1: List Concatination
l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12,l21)

print('...........................')

# Concept 2: List Replication
l1 = [0]*10
l2 = [1,2,3]*5
print(l1)
print(l2)

print('............................')

#Concept 3: Logical Operators in List
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(l1==l2)
print(l2==l3)
print([1,2]<[2,1]) # 1st postion of one list is compared with the 1st postion of the other list
print([1]<[1,2,3])
print([2,3]<[3])
print([]<[1])

print('.........................................')

#Concept 4: Mutability

l = [1,2,4]
print(l)
l[2]=3    # Lists are Mutable, we can modify lists
print(l)

s = 'abce'
print(s[3])   # Although we can access a particular character in the string using it's index but we can't modify that character
#s[3] = 'd' - This is will throw a ERROR as strings are immutable
print(s)

# STRING IS A IMMUTABLE ENTITY IN PYTHON, whearas, LIST IS A MUTABLE ENTITY

print('..............................')

# Concept 5: Memory location in computor 

x = 5         # When we say x = 5, computor allots a certain meomery in the computor system and stores value 5 in that memory and gives a name to that particular memory location as x
y = x         # When we say y = x, computor creates another memory location and stores the value of x in that new memory location and gives it a name y. Which means at this point of time there are 2 different memory locations in the computor system, both has '5' as value in it but the names given to both these memory location are different, 'x' for first memory location and 'y' for second memory location
x = 10        # When we say x = 10, computor replaces the existing value at memory location x from 5 to 10, and memory location y stays untounched with value 5 stored in it.
print(x,y)


# In case of list, computor behaves differently as compared to simple variables
l1 = [1,2,3]  #When we say l1 = [1,2,3], computor allots a certain memory in the computor system and stores this particular list with these 3 values i.e 1,2,3 inside it and gives it a name l1
l2 = l1    # when we say l2 = l1, instead of creating a new memory location, computor simply adds one more name to that same memory location which was created earlier, which means after executing this l2 = l1 , computor still has one meomary location where 1,2,3 are stored in a list
l1[0] = 100  # Now as there is only 1 meomary location and it has 2 different name so if something is changed in any of the list i.e. l1 or l2 in this case then it is automatically reflected in the other list too, that's why while printing l1,l2, we are seeing the same output i.e. [100,2,3]
print(l1,l2)  # Expected: [100,2,3] [1,2,3] But we got [100, 2, 3] [100, 2, 3]  --- Why? - Reason is in above lines!

# Question: How to create a seperate copy of l2 in order to solve the above problem, so that l2 can have it's own different memory location - there are 3 different ways to do that:

l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()

l2[0] = 100
l3[1] = 200
l4[2] = 300

print(l1,l2,l3,l4)

print('..................................')

# Concept 6: This belongs to above concept only: Using a python program, how to figure out whether 2 diffent variables are pointing at a same memeory location or at a 2 different memory location? - Solution is 'is' operator

l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l.copy()
l5 = l1
print(l1 is l2)  # False
print(l1 is l3)  # False
print(l1 is l4)  # False
print(l1 is l5) # True: means l1 and l5 are simply 2 different names given to the same memory location

print('...........................')

# Concept 7: How list behave when we pass list variable as an argument to a function

def add(x):
  x = x + 1  # Local x
  return x

x = 5   # Global x
print(add(x))  # Output: 6  # Local
print(x)       # Output: 5  # Global

def addlist(y):
  y.append(1)
  return y

y = [5]
print(addlist(y))  # Output: [5,1]   # Call by Referance
print(y)       # Output: [5,1] 
# As both output in case of list are same, which means list behave in different manner as compared to integers
# If the function argument is of mutable type then it is called by referance otherwise it is called by value, that's why, in case of list, it was call by referance and in case of integer, it was call by value

print('..............................')

# Concept 8: List Methods

l = [1,2,3]
print(l)

l.append(4)
print(l)

l.remove(2)
print(l)

x = l.copy()
print(x,l)

l1 = [1,2,3]
print(l1)

l1.append(4)
print(l1)

l1.insert(2,9)  # l.insert will gonna insert the value 9 at 2nd index of that particular list
print(l1)

l2 = [1,2,3,4,5]
print(l2)

l2.remove(2)
print(l2)

l2.pop(2)   # l2.pop removes the value at index 2nd of the list and will give the remaning list as the output
print(l2)

l3 = [2,39,23,0,-9,88,1,0]
l3.sort()      # sort will going to sort the list in ascending order
print(l3)

l4 = [2,39,23,0,-9,88,1,0]
l4.reverse()    # reverse will going to reverse the list completely as from back to front
print(l4)

l5 = [2,39,23,0,-9,88,1,0]
l5.sort(reverse = True)         
print(l5)


# l.sort(reverse, key) - This is general form of sort()

## The sort() method can take two optional keyword arguments:
# reverse - By default False. If True is passed, the list is sorted in descending order.
# key - Comparion is based on this function.