# Nested for loop

mann = 'VIBGYOR'
meet = 'VIBGYOR'
count = 0

for i in range(7):
  for j in range(7):
    print(i,j,mann[i],meet[j])
    count = count + 1
print(f'Total no. of combination are {count}.')