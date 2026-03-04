# Concept-1: 'end': To print result in a single sentence:

for x in range(10):
  print(x, end = ' ')  # There is always this 'end' paramenter in print statement with its default setting as \n which means new line.
  
print(end='\n');

# Concept-2: 'sep': To print seperating character which we want:

d = 29
m = 8
y = 2003
'''print('Today\'s date is',d,m,y)''' # it's result will be: Today's date is 29 8 2003
# We are getting space between each parameter into the print statement because there is a feature of 'sep' present there whose default setting is space.

'''print('Today\'s date is',d,m,y,sep = '/')''' # it's result will be: Today's date is/20/8/2003, to remove the slash after is, we need to write the below code:
print('Today\'s date is', end = ' ')
print(d,m,y, sep = '/')

# Concept-3: Formatted printing

num = int(input('Enter the number:'))
for i in range(1,11):
  #print(num,'X',i,'=',num*i) # our normal method
  #print(f'{num} X {i} = {num*i}') # 'f' print method
  #print('{0} X {1} = {2}'.format(num,i,num*i)) # print using format function
  print('%d X %d = %d'%(num,i,num*i)) # print using string modulo operator       #'d' stands for integer

# Concept 4: format specifier using formatted printing

pi = 22/7
print(f'Value of Pi is {pi}')
print('Value of Pi is {0}'.format(pi))
print('Value of Pi is %f'%(pi)) # here we will write 'f' instead of 'd' because our value is in fraction.
                                # Also you can see the limitation of '%f' in string modulo operator is it only able to answer till 6 decimal places only but other two are giving answer to more decimal places.

'''Now I want the answer of 'pi' only till 2 decimal places then we can do that in the following way:'''

pi = 22/7
print(f'Value of Pi is {pi:.2f}')
print('Value of Pi is {0:.2f}'.format(pi))
print('Value of Pi is %.2f'%(pi))

# Concept 5: Pattern printing using format printing (format specifier)

print('{0}'.format(1))
print('{0}'.format(12))
print('{0}'.format(123))
print('{0}'.format(1234))
print('{0}'.format(12345))

# Now if we can right align the above pattern by following method:

print('{0:5d}'.format(1))        # 'd' stands for integer
print('{0:5d}'.format(12))
print('{0:5d}'.format(123))
print('{0:5d}'.format(1234))
print('{0:5d}'.format(12345))