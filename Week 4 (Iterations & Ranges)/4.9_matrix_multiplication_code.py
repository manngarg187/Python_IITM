# Multiplication of Matix

r1 = [2,4,2]
r2 = [6,2,9]
r3 = [23,23,3]

s1 = [28,8,9]
s2 = [4,2,9]
s3 = [2,5,10]

A = []
A.append(r1)
A.append(r2)
A.append(r3)

B = []
B.append(s1)
B.append(s2)
B.append(s3)

print(A)
print(B)

# We need to find A*B

C = [[0,0,0],[0,0,0],[0,0,0]]
dim = 3

#C[2][1] is the dot product of the 2nd row of A and 1st column of B

for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      C[i][j] = C[i][j] + A[i][k]*B[k][j] 
      
print(C)

'''
Shortcut using the Numpy library:
import numpy
X=numpy.mat(A)  (ofcourse you must have written A and B first)
Y=numpy.mat(B)
print(X*Y)'''