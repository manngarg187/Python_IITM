a = int(5.8)
b = int("10")

print(a, type(a))
print(b,type(b))

print("--------------")

c = float(4)
d = float("22")

print(c,type(c))
print(d,type(d))

print("---------")

e = str(9)
f = str(7.9)

print(e, type(e))
print(f,type(f))

print("--------------")

g = bool(7)
h = bool(0) 
i = bool(-7)

print(g,type(g))
print(h, type(h)) 
print(i,type(i))
#bool(0) is false because whenever a computer converts a integer value to boolen, all values except 0 are considered as true. Whereas Zero is the only value which will give us the boolean representation as False.

print("------------------")

j = bool(8.4)
k = bool(0.0)
l = bool(-4.8)

print(j,type(j))
print(k,type(k)) #bool(0.0) is false due to same reason as above
print(l,type(l))

print("--------------")

m = bool("mann")
n = bool("10")
o = bool("-5.3")
p = bool("0") #bool("0") is True because it's a string and for every string other than an empty string, the value is True.
q = bool("") # Only when we convert an empty string to boolen datatype, it results in False.

print(m, type(m))
print(n,type(n))
print(o,type(o))
print(p,type(p))
print(q,type(q))