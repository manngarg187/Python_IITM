# Answer 1
def count(l):
  alp = 'abcdefghijklmnopqrstuvwxyz'
  ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower = 0
  upper = 0
  word = 1
  for each in l:
    if each in ALP:
      upper = upper + 1
    if each in alp:
      lower = lower + 1
    if each == ' ':
      word = word + 1
  total = len(l)
  return upper,lower,total,word

print(count('Functions could have no parameters'))