# Types of Arguments

#1. Positional Arguments

def ram(a,b,c):
  return a + b - c
print(ram(20,70,10))

#2. Keyword Arguments

def syam(c,a,b):
  return a + b - c
print(syam(a = 20, b = 70, c = 10))

#3. Default Arguments

# default arguments help the variable take the values even when we miss to write the corresponding argument of it

def krishan(c, a = 20, b = 10):
  return a + b - c
print(krishan(40))
print(krishan(40,10,50)) 
print(krishan(a = 70, b = 100, c = 65))