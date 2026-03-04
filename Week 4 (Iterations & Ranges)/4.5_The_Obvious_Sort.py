# we will learn one of the way of sorting! It's only for practice, while coding we have to use it's shortcut only i.e. l.sort()
l = [5,44,88,2,383,43,9,99,22,10,0]

x = []

while(len(l)>0):
  min = l[0]    # earlier I wrote min = 0
  for i in range(len(l)):
    if l[i]<min:
      min = l[i]
  x.append(min)  # earlier I have equated x = x.append(min)
  l.remove(min)  # earlier I have equated l = l.append(min)

print(x)
print(l)