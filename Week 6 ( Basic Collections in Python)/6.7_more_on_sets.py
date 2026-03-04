st = {1,2,3,4,5,1,2,3,5}
print(st)         #1. Set do not allow dublicate values

#2. Set is an unordered entity, set is simplely a collection of values: print(st[0]) - this will going to throw an error

#3. Third, with respect to mutability set is peculiar. Set itself is mutable but every value inside the set has to immutable and hashable, which means we can add values in a set but those values should be immutable and hashable, hence we cannot add a dictionary, a list or a non-hashable tuple to a set.

#4. We can iterate over set

#5.Set Methods: The concept  of set in python is derived from mathematical  sets. Therefore, Python set also support  all those operations, which we usually perform  using mathematical sets like subset, superset,  union, intersection, difference and so on. All  these mathematical operations can be implemented using Python sets in two different ways. Either  using a specific operator or using set methods.

A = {1,3,5}
B = {1,7,8,3,-2,5,999}
print(A.issubset(B))
print(A.issuperset(B))

C = {1,2,3}
D = {2,7,1,99}
U1 = C.union(D)       # Method 1: Set method
U2 = C | D            # Method 2: By using operator, here '|' is the specfic operator in python for union
print(U1,U2)

I1 = C.intersection(D)  # Method 1: Set method
I2 = C & D              # Method 2: By using operator, here '&' is the specfic operator in python for intersection
print(I1,I2)

Dif1 = D.difference(C)      # Method 1
Dif2 = D - C                # Method 2
print(Dif1,Dif2)

# Method to insilazie set and to add elements in set:
a = set()
print(a)

a.add(1)
a.add(-78)
print(a)