#!/usr/bin/env python
# coding: utf-8

# In[1]:


from abc import ABC,abstractmethod     #we import ABC,abstractmethod from abc.


# In[2]:


class ss(ABC):                           #abstraction means hiding the implementation part and showing the declaration part.
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
        
class dd(ss):
    def display(self):
        print("hello")
    def show(self):
        print('bye')
obj=dd()
obj.display()
obj.show()


# In[ ]:




