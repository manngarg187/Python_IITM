# Finding a '0' in a list via Recursion. Print 0 (False) if '0' is not there in the list and Print 1 (True) if '0' is there in the list

def find0(L):
  if len(L)==0:
    return 0
  if L[0]==0:
    return 1
  else:
    return find0(L[1:len(L)])

print(find0([3,5,0,2,4545,-98]))
print(find0([77,8,-2,9,8,1]))

# Please NOTE that this is not an efficient code, we will see this later