#find out the minimum most element in list l
#append that to a new list x
#remove the minimum most element in the list l

# Way 1 (Harder Way: We need to avoid this from now on):

def obvious_sort(l):
  x=[]
  while len(l)>0:
    mini = l[0]
    for i in range(len(l)):
      if l[i]<mini:
        mini = l[i]
    x.append(mini)
    l.remove(mini)
  return x

l = [44,2,-9,27,222]
print(obvious_sort(l))


# Way 2 (Easier Way: We need to get use to solve our problems using this - Modular Approach)

#Step 1: find out the minimum most element in list l
def mini_list(l1):
  mini=l1[0]
  for i in range(len(l1)):
    if l1[i]<mini:
      mini = l1[i]
  return mini    # I forgot to return mini here

#Step 2: Append mini to new list y and remove mini from list l
def obvious_sort1(l1):
  y=[]
  while(len(l1)>0):
    mini=mini_list(l1)
    y.append(mini)
    l1.remove(mini)
  return y

l1 = [33,9,-1,334,8]
print(obvious_sort1(l1))

#We just learnt that breaking our problem into smaller modules and solving them makes it easy on our mind.