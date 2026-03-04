d = {}
d['mann'] = 98733
d['meet'] = 38289
d['ansh'] = 77880
print(d)
print(d['meet'])

print('........................')

malgudi = ['My','name','is','Mann','Garg','I','love','to','explore','beautiful','secrets','of','this','world','Presently','I','am','pursuing','a','data','science','course','from','iitm']

s = set(malgudi)
print(s)
d1 = {}
for x in s:
  d1[x]=0
print(d1)

max = 0
maxword = ''

for x in malgudi:
  d1[x]=d1[x]+1
  if max<d1[x]:
    max = d1[x]
    maxword=x

print(d1)
print(max)
print(maxword)

print('..............................')

d2 = {}
d2['mann']=[70,76,24,60,'mann.iitm23@iitm.com']
d2['manas']=[80,29,100,99,'manas.iitm98@iitm.com']
d2['advit']=[44,99,95,100,'advit.iitm654@iitm.com']
print(d2)
print(d2['manas'])
print(d2['advit'][2])
print(d2['advit'][4])