#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fun(name):
    print('hello'+name)


# In[9]:


fun('good')


# In[10]:


def add_fun(num1,num2):
    return num1+num2


# In[11]:


result=add_fun(1,2)


# In[12]:


result


# In[13]:


def say_hello(name):
    print("hello {}".format(name))


# In[15]:


say_hello('Huh')


# In[18]:


def shu(name="default"):
    return(name)


# In[19]:


re=shu()


# In[20]:


re


# # login functions

# In[24]:


2 % 2 == 0


# # mod returns the remainder

# In[23]:


2 % 3


# In[25]:


20 % 2 == 0


# In[30]:


def check_list(num_list):
    for i in num_list:
        if i%2==0:
            return True
        else:
            pass
    return False    


# In[31]:


check_list([1,2,3])


# In[32]:


check_list([1,1,1])


# In[33]:


type(check_list)


# # Now instead of returning boolean value, we will return the actual value

# In[39]:


def check_list(new_list):
    
    even_number=[]
    
    for i in new_list:
        if i%2==0:
            even_number.append(i)
        else:
            pass
        
    return even_number    


# In[40]:


check_list([1,2,3])


# In[41]:


check_list([2,3,4])


# # Tuples

# In[42]:


s_p=[('App',200),('Sam',200),('Web',300)]


# In[43]:


for i in s_p:
    print(i)


# In[44]:


for i,j in s_p:
    print(i)


# In[45]:


for i,j in s_p:
    print(j)


# In[2]:


work_hours=[('App',200),('Sam',200),('Web',300)]


# In[12]:


def employee_check(work_hours):

    current_max=0
    employee_of_month=""

for employee,hours in work_hours:
    if hours > current_max :
        cureent_max=hours
        employee_of_month=employee
    else:
        pass
return (employee_of_month,current_max)    


# In[46]:


li=['dileep','shubham']


# In[52]:


lis=[]
for i in li:
    print(i[3])


# In[19]:


def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)


# In[20]:


employee_check(work_hours)


# In[34]:


def even(num):
    
    even_num=[]
    
    for i in num:
        if i%2==0:
            even_num.append(i) 
        else:
            pass
    return even_num    


# In[35]:


even([1,2,3,4,5])


# In[36]:


def cube(num):
    cube=[]
    for i in num:
        if i%3==0:
            cube.append(i)
        else:
            pass
        
    return cube


# In[37]:


cube([1,3,6,9,8])


# In[ ]:


s_p=

