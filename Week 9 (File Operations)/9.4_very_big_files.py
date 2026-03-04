 # Sir took an example of a big text file = 12 GB 

# This file got stuck when we tried to open it and sir said that, No editor can open such a long text file

# Golden Point:  We can't open this file But, No Matter how big the file is, we can always read from it via using .readline() command

#This are just notes so don't try to run them
f = open('phone_large.txt','r')
f.readline()  ---> 1st line
f.readline()  ---> 2nd line
f.readline()  ---> 3nd line
.
.
.          
          or

for i in range(10000):
  s= f.readline()
  print(s)

# Golden Point: Irrespective of how big the file is, it may not open easily but we can go line by line within it

# That's how movie files works. Movie files are a list of pitures (some may contain millions of pitures)