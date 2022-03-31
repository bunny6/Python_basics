#!/usr/bin/env python
# coding: utf-8

# # If, elif, else

# In[6]:


num = 5
if num == 6 :
    print('Number is 6')
    
elif num>6:
        print('Number is greater then 6')
        
else:
            print('Number is less then 6')


# In[15]:


d=[1,2,3,4,5,6,7,8,9,10]
for i in d:
    print("6 *",i,':',6*i)
    


# In[21]:


name="Shubham"
if name=="Ajay":
    print('Hey Ajay')
elif name=="Shubham":
    print('Not You boy')
else:
        print('Ajay is not available')


# # For loop

# In[22]:


list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(6*i)


# In[26]:


for i in list1:
    if i%2==0:
        print('Even no. is',":",i)
    else:
        print('Odd number is:',i)
        
    


# In[27]:


st="Hello World"
for i in st:
    print(i)


# In[28]:


d={'K1':1,"k2":2,'k3':3}


# In[29]:


d


# In[30]:


for i in d:
    print(i)


# In[33]:


for k,v in d:
    print(v)


# # While loop

# In[37]:


x=1
while(x<11):
    print('6 *',x,6*x)
    x=x+1


# In[38]:


ms="Hello"
for i in ms:
    print(i)


# In[56]:


x=0
while x<5:
    print("x is",x)
    x=x+1
else:
        print("end")


# In[62]:


sy=[1,2,3]
for i in sy:
    pass
print('end')


# In[ ]:




