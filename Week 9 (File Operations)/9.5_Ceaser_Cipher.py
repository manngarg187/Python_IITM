# Caesar Cipher: Here we are encrpting the file sherlock.txt by shifting it's each alphabet by 3 postions and making a new file named as encryted_sherlock.txt. 'a' will convert to 'd', 'b' will convert to 'e',.....,'y' will convert to 'b' and 'z' will convert to 'c'

import string

def create_caesar_dictionary():
  l=string.ascii_lowercase
  l=list(l)
  d={}
  for i in range(len(l)):
    d[l[i]] = l[(i+3)%26]
  return d

f = open('sherlock.txt','r')
g = open('encryted_sherlock.txt','w')
d=create_caesar_dictionary()

c=f.read(1)
while (c!=''):
  g.write(d[c])
  c=f.read(1)

f.close()
g.close()