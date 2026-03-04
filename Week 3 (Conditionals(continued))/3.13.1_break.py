# xyx123@iitm.in - We want to print all the letters individually in the user name of an email id
email = input('Enter your email id: ')
for c in email:
  if(c=='@'):
    break
  print(c)