# This is popularly known as Cesar Ciphar in crptograpy

alpha = 'abcdefghijklmnopqrstuvwxyz'
s= 'zebra'  # expected output is: afcsb (basically each letter should be shifted by 1 in the output)
i=0
m=1 # 'm' decides that by how much position each letter of a particular word in 's' should be shifted.
t=''
t=t+(alpha[((alpha.index(s[i]))+m)%26])
t=t+(alpha[((alpha.index(s[i+1]))+m)%26])
t=t+(alpha[((alpha.index(s[i+2]))+m)%26])
t=t+(alpha[((alpha.index(s[i+3]))+m)%26])
t=t+(alpha[((alpha.index(s[i+4]))+m)%26])
print(t)