#!/usr/bin/env python
# coding: utf-8

# In[3]:


fib=[1,2]
for i in range(2,100):
    fib.append(fib[i-1]+fib[i-2])
    
print(fib[-1])


# In[ ]:




