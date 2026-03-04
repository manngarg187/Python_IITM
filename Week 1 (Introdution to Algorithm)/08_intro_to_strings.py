#Understand the ideas of string concatenation, indexing and slicing.
a="suprise"
b="introduction"
print(a+b) #concatination
print(a[1]) #indexing
print(b[3:9]) #slicing

d="038492084904"
c=d[2] #it's a string right now
e=d[5]  #it's a string right now
print(c+e,type(c+e))

f=int(d[2]) # here string is converted to integer first
g=int(d[5]) # here string is converted to integer first
print(f+g,type(f+g))