#Matrix addition by first principles
# first principle  just means that we will be writing the whole code by ourselves rather than using the libraries

dim = 3
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

# I need to add A and B

C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
  for j in range(dim):
    C[i][j] = A[i][j]+B[i][j]

print(C)