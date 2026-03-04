# Find the grade of students based on the given marks between 0 to 100
marks = int(input('Enter marks: '))
if (marks>=0 and marks<=100):
  if(marks>=90):
    print('A')
  if(marks<90 and marks>=80):
    print('B')
  if(marks<80 and marks>=70):
    print('C')
  if(marks<70 and marks>=60):
    print('D')
  if(marks<60):
    print('E')
else:
  print('Invalid input')