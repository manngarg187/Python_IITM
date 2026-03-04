# Let us write a few functions on lists

def list_min(l):
  mini = l[0]
  for i in range(len(l)):
    if l[i] < mini:
      mini = l[i]
  return mini

def list_max(l):
  maxi = l[0]
  for i in range(len(l)):
    if l[i]>maxi:
      maxi = l[i]
  return maxi

def list_appendbefore(l,z):
  newl = []
  for i in range (len(z)):
    newl.append(z[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl

'''
# Just a 
def list_appendbefore(l,z):
  newl = []
  newl = newl + z
  newl = newl + l
  return newl
'''

def list_appendafter(l,z):
  newl = []
  for i in range (len(l)):
    newl.append(l[i])
  for i in range(len(z)):
    newl.append(z[i])
  return newl

def list_average(l):
  sum = 0
  for i in range(len(l)):
    sum = sum + l[i]
  avg = sum/len(l)
  return avg


l = [22,-8,100,-123,298]
z = [4,-9,999]
print(list_min(l))
print(list_max(l))
print(list_appendbefore(l,z))
print(list_appendafter(l,z))
g = [3,88,2,18]
print(list_average(g))