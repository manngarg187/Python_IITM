# range always has 3 parts i.e. start,end,step
# 'end' value is computlsory in range but for 'start' & 'step' default setting is '0' & '1' respectively

for i in range(9,-1,-2):
  print(i)

# for loop code without range:

country = 'India'
for letter in country:        # compare to 'for each' loop which we studied in computational thinking course
  print(letter)               # for each is mainly used over "Strings"
'''
In the above code following is written in a more efficient way:
print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])''' 