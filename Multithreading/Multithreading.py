#!/usr/bin/env python
# coding: utf-8

# In[2]:


from threading import *
from time import sleep


# In[6]:


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
obj1=Hello()
obj2=Hi()

obj1.start()  #inside thread there is a method in run. Start will execute like obj1 with thread 1 and obj2 with thread 2
obj2.start()


# In[ ]:


class Add(Thread):
    def run(self,num1,num2):
        for i in df:
            print("num1+num2")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
obj1=Hello()
obj2=Hi()

obj1.start()  #inside thread there is a method in run. Start will execute like obj1 with thread 1 and obj2 with thread 2
obj2.start()

