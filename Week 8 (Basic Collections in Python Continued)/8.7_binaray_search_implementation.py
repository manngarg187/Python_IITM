def obvious_search(L,k):
  # Check if the given element k is present in list L or not
  for x in L:
    if x==k:
      return 1
  return 0

# Question: Can we find a element k in list L faster then the above obvious sort method

def binary_search(L,k):
  # This is the alternative for the obvious search. It does exactly what is expected from the obvious_search, but in a an effective way. This method is popularly known as Binary Search.

  # We want to shrink our list
  # We will do that using a while loop.

  begin =0   #first element in L. L[0]
  end=len(L)-1  # the last element in L is in len(L). L[len(L)-1]

  #Use a while loop to look at the list and keep halving it.
  while(end-begin>1):
    #we will handle the case when the number of elements is less than or equal to 1

    # Compute the mid which is the mid point of begin to end.
    mid = (begin + end)//2

    # mid is indeed k, then we return True and stop the code.
    if (L[mid]==k):
      return 1

    # if the middle element is greater than k, then cut the right side and retain the left side.
    if (L[mid]>k):
      end=mid-1

    # if the middle element is less than k, then cut the left side and retain the right side.
    if (L[mid]<k):
      begin= mid+1

  #This is outside of the while loop. If we are here, it means that we haven't found the element. Also, if we are here, it means that the while condition is violated. While means end-begin is less than or equal to 1.

 #if it is equal to 1, then there is exactly two elements
  if (L[begin]==k) or (L[end]==k):
    return 1
  else:
    return 0

'''
## Write the below code in your console and check the time
L = list(range(1000*1000*10))
import time
a=time.time();print(obvious_search(L,-1));b=time.time();print(b-a)     # It gave me answer in 1.1 seconds
b=time.time();print(binary_search(L,-1));b=time.time();print(b-a)      # It gave me answer in 0.0003 seconds
'''