# 3rd way of importing library:

from calendar import month, calendar # here the problem is that we can only use the selected feature from whole calendar library, like here we have selected 2 features i.e month & calendar.
print(month(2031,3))
print(calendar(2012))

''' We can also write:
    
    from calendar import month as m
    print(m(2031,3))
'''