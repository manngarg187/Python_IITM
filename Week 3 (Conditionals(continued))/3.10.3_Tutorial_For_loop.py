# Reverse the digits in the given no.  # For loop
# Although for this question while loop is prefered but we are doing it by for each method:

num = int(input('Enter the number: '))
absStrNum = str(abs(num))
rev = ''
for i in absStrNum:
  rev = i + rev
if(num >= 0):
  print(rev)
else:
  print('-' + rev)