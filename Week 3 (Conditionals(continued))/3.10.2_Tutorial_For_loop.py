# Find No. of digits in the given number   # for loop 
# Although while loop is preferred for this problem, we are doing it anyhow by using for each technique

num = abs(int(input('Enter the number:')))
strNum = str(num)
digits = 0

for a in strNum:
  digits = digits + 1
print(digits)