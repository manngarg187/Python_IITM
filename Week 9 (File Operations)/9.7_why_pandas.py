# Code without using Pandas:

'''
f = open('scores.csv','r')
scores = f.readlines()[1:]
max = 0
for records in scores:
  field = records.split(',')
  if int(field[8])>max:
    max = int(field[8])
print(max)
'''
### NOTE: Pandas is a external library, while Calander,random, etc are part of python programming language

# Code using Pandas:  it just becomes a 3 line code! wow!

import pandas as pd
scores = pd.read_csv('scores.csv')
print(scores['Total'].max())

# Other feature of pandas

#print(scores)
#print(scores.shape)
#print(scores['Total'].max())
#print(scores['Total'].min())
#print(scores['Total'].mean())
#print(scores['Total'].sum())
#print(scores['Total'].sort_values())   -- This will sort the values in acending order
#pirnt(scores['Total'].sort_values(ascending=False))   -- This will sort the values in decending order
