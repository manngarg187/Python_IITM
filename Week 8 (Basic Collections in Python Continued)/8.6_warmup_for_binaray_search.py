def obvious_search(L,k):
  # Check if the given element k is present in list L or not
  for x in L:
    if x==k:
      return 1
  return 0
'''
## Write the below code in your console and check the time
L = list(range(100000000))
import time
a=time.time();print(obvious_search(L,999999999999));b=time.time();print(b-a)
'''
# Question: Can we find a element k in list L faster then the above obvious sort method