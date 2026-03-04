# Find the grade of students based on the given marks between 0 to 100
marks = int(input('Enter marks: '))
if (marks>=0 and marks<=100):
  if(marks>=90):
    print('A')
  elif(marks>=80): # In Python, elif is short for "else if" and is used when the first if statement isn't true, but you want to check for another condition.
    print('B')
  elif(marks>=70):
    print('C')
  elif(marks>=60):
    print('D')
  else:
    print('E')
else:
  print('Invalid input')