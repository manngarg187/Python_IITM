# Question 2

# Menu Driven Program

pi = 22/7
def cir_area(r):
  return pi*(r**2)

def cir_per(r):
  return 2*pi*r

def rec_area(l,b):
  return l*b

def rec_per(l,b):
  return 2*(l+b)

if input()=='circle':
  if input()=='area':
    a = float(input())
    print(cir_area(a))
  if input()=='perimeter':
    a = float(input())
    print(cir_per(a))
if input()=='rectange':
  if input()=='area':
    c = float(input())
    d = float(input())
    print(rec_area(c,d))
  if input()=='perimeter':
    e = float(input())
    f = float(input())
    print(rec_per(e,f))
if input()=='exit':
  sys.exit