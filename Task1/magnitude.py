#!/usr/bin/env python
# coding: utf-8

# Sirius data
# apparentMagnitude = -1.46
# absoluteMagnitude = 1.45
# 
# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly
# 

# In[4]:


m = float(input("Input the apparent magnitude: "))
M = float(input("Input the absolute magnitude: "))

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

print(f"The distance of Sirius is {d} ly")


# In[ ]:




