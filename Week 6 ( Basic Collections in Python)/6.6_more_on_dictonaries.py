# d = {key : value}
# Every key inside a dictionary is different from one another
# Value can be same
# Key of dictionary should be immutable and hasable
# integer,float,boolean,string, etc... can be used a key inside a dictionary
# But list, another dictionary can't be used as key inside a dictionary as they are mutable
# Tuple can be and cannot be used as key in dictionary, basically hashable tuple can be used as key as they are immutable from within too but not-hashable tuple cannot be used as key as they are mutable from within

# Value inside a dictionary can be anything, there are no restriction on it

# As dictionary is also mutable entity like list, all the different properties we studied for list are also applicable for dictionary too.

# Concept 1: How to iterate over a dictionary

d = {0:0,1:1,2:4,3:9,4:16}
print(d)
for key in d:           # here it is not necessary to use 'key', we can even use 'each','m','h8',etc instead of 'key', it's just to explain
  print(key, d[key])

# Concept 2: Dictionary specific methods

d = {0:0,1:1,2:4,3:9,4:16}
print(d.keys())
print(d.values())
print(d.items())