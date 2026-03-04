# Find No. of digits in the given number

num = abs(int(input('Enter the number:')))
digits = 1
while(num>9):
  num = num//10
  digits = digits + 1

print(digits)