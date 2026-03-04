# Now, we are writing a code to do binary search by using the recursion method
def rbinarysearch(L,k,begin,end):
  if begin==end:
    if begin==k:
      return 1
  if end-begin==1:
    if (L[end]==k) or (L[begin]==k):
      return 1
  if (end-begin)>1:
    mid=(begin+end)//2
    if L[mid]==k:
      return 1
    if L[mid]>k:
      end=mid-1
    if L[mid]<k:
      begin=mid+1
  if end<begin:
    return 0
  return rbinarysearch(L,k,begin,end)
  
# This error came when I exuted the following in console:
  '''
   L = list(range(1000*1000*10))
   import time
   a=time.time();print(rbinarysearch(L,-1,0,len(L)-1));b=time.time();print(b-a)
  '''
# RecursionError: maximum recursion depth exceeded in comparison

# Note: Recursion will not always work in Python Beyond a limit (Default limit is 999), although we can change this default limit in python for Recursion by using the sys library. Generally a limit is set on Recursion as in somecases it can go on and on...So a finite limit is important.