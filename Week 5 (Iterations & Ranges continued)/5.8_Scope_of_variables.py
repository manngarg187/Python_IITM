# Concept 1: Call by Value and Scope of Variable
# Concept 2: Local and Global Variable

def myFunction1():
  global x
  x = x*2
  print("Value of x in function 1", x)

def myFunction2():
  global x
  x = x*3
  print("Value of x in function 2",x)

x = 5  # This is a global variable
print("Value of x before function call", x)
myFunction1()
myFunction2()
print("Value of x after function call",x)

print('__________________________________')


def myFunction3(y):  #here vaiable y in myFunction3 is only accisable in myFuction3  - Here y is a 'Local Variable'
  y=y*2
  print('Value of y in function 3',y)

def myFunction4(y):    #here vaiable y in myFunction3 is only accisable in myFuction4 - Here y is a 'Local Variable'
  y=y*3
  print('Value of y in function 4',y)

y=7  # This is a Global variable
print('Value of y before function call',y)
myFunction3(y)
myFunction4(y)
# Here in the above 2 lines, these fuctions are not taking whole y=7 rather they are only considering the value of y i.e. 7
print('Value of y after function call',y)