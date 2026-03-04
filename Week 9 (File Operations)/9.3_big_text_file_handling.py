
       # There are some notes of this lecture in ipad

       # This code will note run, it is just for practise and notes purpose

f = open('directory.txt','r')
flag = 0
s = '0'
while s != '':
  s = f.readline()
  if s != '':
    n=int(s)
    if n==9873988871:
      print('The number was found')
      flag = 1
      break
if flag ==0:
    print('The number was NOT found')