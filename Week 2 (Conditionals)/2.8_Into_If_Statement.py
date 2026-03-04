#if statement

#Example: Let us consider the movie Avengers. It's a 13+ movie.

print('Enter your year of birth')
year_of_birth = int(input())

current_year = 2023

age = current_year - year_of_birth

if(age<13):
  print('You are under age!')
  print('First become older enough.')
else:
  print('You are older enough to watch this movie')
  print('Enjoy!')