def mini(L):
  min = L[0]
  for i in range(len(L)):
    if L[i]<min:
      min = L[i]
  return min

def sort(L):
  if L == [] or len(L) == 1:
    return L
  min = mini(L)
  L.remove(min)
  return [min]+sort(L)

print(sort([23,545,-88,5,243,1,0]))