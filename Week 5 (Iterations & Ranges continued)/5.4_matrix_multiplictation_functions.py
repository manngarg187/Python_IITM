# Initialize C to zero
# I need to consider two matrices A and B
# I need to find the dot product of 2 lists
# I need to pick ith row and jth colum in a matrix.

def initialize_mat(dim):
  C = []
  for i in range(dim):
    C.append([])
  for i in range(dim):
    for j in range(dim):
      C[i].append(0)
  return C

'''def dot_product(u,v):
  dot = 0
  for i in range(len(u)):
    for j in range(len(v)):
      if i==j:
        dot = dot + u[i]*v[j]
  return dot
'''

# better code for above part:
def dot_product(u,v):
  dim = len(u)
  dot = 0
  for i in range(dim):
    dot = dot + (u[i]*v[i])
  return dot

def row(A,i):
  dim=len(A)
  l=[]
  for k in range(dim):
    l.append(A[i][k])
  return l

def col(A,j):
  dim=len(A)
  l=[]
  for k in range(dim):
    l.append(A[k][j])
  return l  #( I had earlier done intendation error here, I wrote return l into the for loop)

def mat_multiply(A,B):
  dim = len(A)
  C=initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      C[i][j] = dot_product(row(A,i),col(B,j))
  return C

A = [[1,3,8],[2,8,9],[7,2,9]]
B = [[2,9,1],[5,1,1],[1,2,9]]
print(mat_multiply(A,B))

'''
### To Check the above answer easily, we can use numpy ###
A = [[1,3,8],[2,8,9],[7,2,9]]
B = [[2,9,1],[5,1,1],[1,2,9]]
import numpy
A = numpy.mat(A)
B = numpy.mat(B)
C = A*B
print(C)
'''