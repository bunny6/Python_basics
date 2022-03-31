#!/usr/bin/env python
# coding: utf-8

# In[2]:


def topten():
    yield 1
    yield 2
    yield 3
    yield 4
values=topten()    
print(values.__next__())
print(values.__next__())


# In[4]:


def topten():
    n=1
    
    while n<11:
        sq=n*n
        yield sq
        n=n+1
        
values=topten()
for i in values:
    print(i)


# In[ ]:




