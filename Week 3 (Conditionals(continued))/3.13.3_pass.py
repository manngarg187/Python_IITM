# First categorize the no. between (0 to 10) in 2 categories - first category in which no. are divisible by 3 and second category in which all the numbers not divisible by 3. Then print the no. which are divisible by 3. I am still not sure what to do with second category.

for x in range(11):
  if(x%3 == 0):
    print(x)
  else:
    pass      # pass is kind of a null statement in python which lets the code to continue 
  

# | Feature        | `continue`                                  | `pass`                             |
# | -------------- | ------------------------------------------- | ---------------------------------- |
# | Meaning        | Skip the rest of the current loop iteration | Do nothing                         |
# | Effect on loop | Immediately jumps to the next iteration     | Loop continues normally            |
# | Purpose        | Control flow                                | Placeholder                        |
# | Use case       | Skip specific cases in loop                 | Empty block where code is required |


'''
==>> Real Reason Developers Use pass

# Usually when writing incomplete code.

# Example:

# for i in range(5):
#     if i == 3:
#         pass   # TODO: handle special case later

# Developer writes structure first, logic later.
'''


# ==>> Another Common Use (Very Important)

# Inside empty functions or classes.

# Example:

# def my_function():
#     pass

# Without pass:

# IndentationError

# Same with classes:

# class Student:
#     pass

