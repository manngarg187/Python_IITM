## Rules for writing varible names:

# or,and,while,.. are called as KEYWORDS
# Keywords can't be used as variables
# Only alphanumeric variables (A,B,...Z,a,b,...z,0,1,2,...9) & underscore (_) can be used in a varible name
# You must start a varible name with a ablphabet or an underscore (numeric starting of a varible name is not allowed)
# Example of what is WRONG:
# 5 = udcw 
# if = 79
# 2a = 89 (to make it right you can right _2a or b2a, etc...)
# Varible names are case sensetive, example:
mann = 2
Mann = 4
MANN = 9
print(mann,Mann,MANN)

#multiple assignment
a,b=3,4 #multiple assignment
print(a,b)
x=y=z=10 #multiple assignment
print(x,y,z)

r,t = 79,23
r,t = t,r
print(r,t)

#deleting a variable = they are used to delete a lot of varibles which we have created so that we can reuse them or 
i=55
print(i)
del i
# print(i) will come not defined as we have not defined any new value to 'i' varible after deleting it

#shorthand operator: 

count=0
count=count+1
count+=1 #(count+=1 means count=count+1, basically count+=1 saves our time) #shorthand operator
print(count)
jam=70
jam=jam/2
jam/=2 #shorthand operator works with all the operators +,-,*,/,...
print(jam)

# in operator: 
# it searches that wether a particular value exist in whole value or not, 
# it is also used by search engines
# result is always a boolean value.

print('alpha' in 'A variable name can only contain alpha-numeric characters and underscores.')
print('alpha' in 'A variable name must start with a letter or the underscore character')

print('.................')
# chaining operators - when we use multiple relational operators in a single statement then it is called as chaining operator. 

b=5
print(10>b>5)
print(10<b<20)
print(5==b>=4)
print(10>b<=9)
print(b<10<b*10<100)