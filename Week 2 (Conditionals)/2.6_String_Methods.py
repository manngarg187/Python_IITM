x = 'mAnnMEEt sTeve Jobs'
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())

y = 'i Have sEt a target till 15 June,2024. it sHoulD be achIVEd.'
print(y.lower())
print(y.upper())
print(y.capitalize()) # capitalize doesn't care about fullstop. It only capitalize the first letter of your string (doesn't matter that string is a paragraph with many fullstops)
print(y.title())
print(y.swapcase())

print('................')

z = 'python'
print(z.islower()) # islower returns TRUE if all the characters in the string are lower case
q = 'Python'
print(q.islower())
w = 'PYThon'
print(w.isupper()) # isupper returns "TRUE" if all the characters in the string are upper case
e = 'PYTHON'
print(e.isupper())
r = 'Python Is A Good Language.'
print(r.istitle()) # istile returns TRUE if the string follows the rules of a title
t = '148'
print(t.isdigit()) # isdigit returns True if all characters in the string are digits
y = '79de330'
print(y.isdigit())
u = 'sght'
print(u.isalpha()) # isalpha returns True if all characters in the string are alphabets
i = 'sfdf39&$'
print(i.isalnum(),i) # isalnum returns True if all characters in the string are alpha-numeric (Alpha numeric includes all samll & capital alphabets and all numbers from 0 to 9)
o = 'aoeigtm29'
print(o.isalnum())

p = '-------Python------------------'
print(p.strip('-')) # strip() returns a trimmed version of the string
print(p.lstrip('-')) # lstrip() returns a left trim version of the string
print(p.rstrip('-')) # rstrip() returns a right trim version of the string
a = '*****Yawn***'
print(a.strip('*'))
s = '****9*****BeHappy***'
print(s.strip('*'))
d = 'apple'
print(d.startswith('A'),d) # startswith() returns True if the string starts with the specified value (It's case sensitive)
f = 'Apple'
print(f.startswith('A'))
print(f.endswith('e')) # endswith() returns True if the string ends with the specified value (It's case sensitive)

g = 'I am hAppy.'
print(g.count('p')) # count() retuns the no. of times a specfied value occurs in a string
print(g.count('a'))
print(g.index('A')) # index() searches the string for a specified value and returns the position of where it was found first in string
print(g.replace('m','NgTP')) # replace() returns a string where a specified value is replaced by a specified value