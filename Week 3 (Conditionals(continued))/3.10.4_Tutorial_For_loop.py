# Find whether a no. is a palindrome or not    # for each method
# Although for this problem while loop was prefered

num = int(input())
absNumStr = str(abs(num))
rev = ''
for i in absNumStr:
  rev = i + rev
if (rev == absNumStr):
  print('Palindrome')
else:
  print('Not Palindrome')