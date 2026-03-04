#Inbuild functions: They are already there in python library itself
print(), input(), len()

#Library functions: We need to use a library to use them, for example: maths.log(), calender.month(), etc
log(), sqrt(), random(), randrange(), calendar(), month()

#String methods (functions): These functions are applied on a string, for example: ''.upper(), etc
upper(), lower(), strip(), count(), index(), replace()

#User Defined functions: as we as a user define the function that what it will do and what will be it's name.
def square(x):
  sqr = x**2
  return sqr

print(square(5))