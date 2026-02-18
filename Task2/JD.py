#!/usr/bin/env python
# coding: utf-8

# In[10]:


from math import *
y1=int(input("Enter the year: "))
m1=int(input("Enter the month: "))
d1=int(input("Enter the day: "))
y0=2026
m0=2
d0=17
def julian(y,m,d):
    JD=367*y-7*floor(floor(y+(m+9)/12)/4)-3*floor((floor(floor(y+(m-9)/7)/100)+1)/4)+floor((275*m)/9)+d+1721029-0.5
    return JD

day=julian(y1,m1,d1)
print('That day is ', day)
today=julian(y0,m0,d0)
birthday=day
age=today-birthday
print('Your age in days is', age)


# In[ ]:




