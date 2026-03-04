# Problem 4: Find the length of longest word from the set of words entered by the user
word = input('Enter a word: ')
maxLen = 0
while(word != '-1'):     # Mistake: Earlier I typed this:  while(word != -1)  -1 is a integer & '-1' is a string
  count = 0
  for letter in word:
    count = count + 1
  if(count > maxLen):
    maxLen = count
  word = input('Enter a word: ')
print('The length of the Longest word is %s' %maxLen)

''' My code:

n = input('Enter the word: ')
biggest = 0
while n != '-1':
  count = 0
  for i in n:
    count = count + 1
  #biggest = 0  - incorrect
  if count > biggest:
    biggest = count
  n = input('Enter the word: ')

print(biggest)
'''