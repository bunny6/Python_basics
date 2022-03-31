#!/usr/bin/env python
# coding: utf-8

# In[3]:



v=lambda a:a%2


# In[4]:


v(2)


# In[5]:


v(19)


# In[6]:


list=[1,2,3,4,5,6]
v=lambda a:a%2


# In[7]:


r=v(5)


# In[8]:


print(r)


# In[15]:


def sum(a,b):
    return a+b


# In[16]:


sum(2,4)


# In[17]:


r=lambda a,b:a+b


# In[18]:


r(2,4)


# In[2]:


list2=[1,2,3,4,5,6,7]


# In[29]:


t=list(filter(lambda a:a%2==0,list2))


# In[3]:


y=list(map(lambda n:n+2,list2))


# In[4]:


print(y)


# In[31]:


num=[1,2,3,4,5,6,7]


# In[32]:


from random import shuffle


# In[33]:


shuffle(num)


# In[34]:


print(num)


# In[1]:


num=[1,2,3,4,5,6,7]
evens=list(filter(lambda n : n%2==0,num))
print(evens)


# In[1]:


listt=[1,2,3,4,5,6]
f=list(filter(lambda n:n%3==0,listt))


# In[4]:


print(f)


# In[ ]:




