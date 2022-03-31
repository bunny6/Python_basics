#!/usr/bin/env python
# coding: utf-8

# # Strings

# In[7]:


my_string='Hello world'      #declaring a string


# In[8]:


my_string[0]


# In[9]:


my='abcdefghij'


# In[10]:


my[2:]                       #slicing


# In[11]:


my[1:3]


# In[13]:


my[::-1]


# In[14]:


my_string.upper()


# In[15]:


print("this is a {} {}".format('good','string'))


# # List

# In[16]:


li=[1,2,3]               #declaring list


# In[17]:


li[0]='New value'


# In[18]:


li


# In[19]:


li[1:]                   #slicing


# In[20]:


li.append('Six')


# In[21]:


li


# In[22]:


li.pop(1)


# In[23]:


li


# # Dictionary

# In[24]:


d={'key1':'Value1','Key2':'value2'}                   #declaring dictionary


# In[25]:


d['key1']


# In[26]:


d['key3']='value3'


# In[27]:


d


# In[28]:


d['key3']


# In[29]:


d1={'Shubham':45,'Dileep':55}


# In[30]:


d1.keys()


# In[31]:


d1.items()


# In[32]:


d1.values()


# # Tuples

# In[33]:


tu=(1,2,3)                         #declaring a tuple


# In[34]:


tu[0]


# In[35]:


tup=('this','is','tuple')


# In[36]:


li=['this','is','list']


# In[37]:


type(tup)


# In[38]:


type(li)


# # Sets

# In[39]:


myset=set('aa')                   #declaring a set. Set return unique value


# In[40]:


myset


# In[41]:


myset.add('a')


# In[42]:


myset


# # Boolean

# In[1]:


True


# In[3]:


False


# In[4]:


type(True)


# In[5]:


1>2


# In[6]:


1==2


# In[7]:


2==2


# In[ ]:




