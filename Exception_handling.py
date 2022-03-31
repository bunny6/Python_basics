#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
try:
    c=a/b
    print(c)
except:
    print("Exception raised")
else:
    print("No exception")
finally:
    print("Program ends")


# In[2]:


a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
try:
    c=a/b
    print(c)
except:
    print("Exception raised")
else:
    print("No exception")
finally:
    print("Program ends")


# # Single exception

# In[3]:


a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))

try:
    c=a/b
    print(c)
except Exception as e:
    print(e)
    


# In[ ]:




