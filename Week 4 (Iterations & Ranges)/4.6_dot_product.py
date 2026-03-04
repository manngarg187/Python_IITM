import random
#write a piece of code to find the dot product

x = [1,7,3,4]
y = [8,6,3,2]

#dot_product = (1*8) + (7*6) + (3*3) + (4*2)

sum = 0
for i in range(len(x)):
  sum = sum + x[i]*y[i]

print(sum)