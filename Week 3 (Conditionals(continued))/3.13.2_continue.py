# xyz123@iitm.in - Print the user name & the domain name in seperate line ( Skip '@')

# continue : It is used to skip the iteration (means whatever is written after continue will be skipped for this particular iteration in this loop).

email = input('Enter the email id: ')
for c in email:
  if (c == '@'):
    print('')   # '' is used to give a line break
    continue
  print(c, end = '')