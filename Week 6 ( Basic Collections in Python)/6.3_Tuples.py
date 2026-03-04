# Tuples is Unchangable whereas a List can be changed
# Tuple takes less storage as compared to Lists.
# When we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple

# Sir took the analogy of a cabourd to explain this topic very well.
# Fixed cabourd = Tuples
# Movable cabourd = Lists
# Movable cabourd has extra wheels which makes it movable when complared to a fixed cabourd so movable cabourd will cost us more as compared to fixed cabourd. Similarly, Tuples takes less space as compared to List.

l = list(range(10))
t = tuple(range(10))
print(l)
print(t)
# l is flexible but t is not in this example

# Sometimes you don't want things to change, you may want to fix the things. There we use Tuples

import string

alp = string.ascii_letters
print(alp)

alpha = tuple(list(alp))
print(alpha)
x = 'mann**$2Garg. INDIA@89!MANN'
x_list = list(x)
print(x_list)
r = []
for each in x_list:
  if each in alpha:
    r.append(each)

print(r)

print('...........................')

l = list(range(10))
t = tuple(range(10))
print(l.__sizeof__())  # 120 bit
print(t.__sizeof__())  # 104 bit