# Concept 1:(Tuples) Packing and Unpacking

# Example 1:
t = 1,2,3             # We haven't wrote these 3 values inside round brackets but still computor converted these 3 values into a tuple, so basically we are packing these 3 values into a single entity called as tuple.
print(t,type(t))

x,y,z = t             # when we say x,y,z = t, we are UNPACKING this tuple into 3 independent integer values, because of which the 2nd print statement is printing 3 independent integers
print(x,y,z)

# Example 2:
m = 5
n = 10
m,n = n,m  # here first python is packing n,m in a tuple on left hand side and then it is unpacking m,n in right hand side, so basically it looks very common to us from outside but all this is going on within it if we go deeper in this
print(m,n)

print('.............................')

# Concept 2

l = [10]
print(l,type(l))

t = (10)       # When we use these round brackets to create the tuple and we only add one value inside it then python consider it as a single value instead of a tuple
print(t,type(t))

# to create a tuple with a single value inside it, we need to add a comma after it

t1 = (10,)
print(t1,type(t1))

print('.......................................')

# Concept 3:

t = ([1,2], ['a','b'])
print(t)
#t[0] = [10,20] # This will throw an ERROR: because As tuple is immutable so we can't change values in tuple
t[0][0] = 87  # Yes, immutablity of tuple is unable to stop us to change value of a list inside a tuple 
print(t)

# Concept 4:

t1 = (1,2,3)         # t1 is hashable - if the values inside tuple are also immutable then the tuple is considered as Hashable
t2 = ([1,2,3],)      # t2 is not hashable - if values inside tuple are mutable then the tuple is refered as Non-Hashable