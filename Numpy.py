#!/usr/bin/env python
# coding: utf-8

# # Array

# In[1]:


import numpy as np    #importing the Numpy library. 'as' means Alternate name.


# In[4]:


a=np.array([1,2,3])      #creating a array.
b=np.array(52)
print(a)                 #printing a array.
print(b)


# In[5]:


type(a)                 #getting the data type.


# In[12]:


c=np.array([[1,2,3],[4,5,6]])     #2d array. Matrix format.


# In[13]:


c                      


# In[14]:


d=np.array([[[1,2,3],[4,5,6]],[[7,8,6],[6,5,6]]])    #23 array. Matrix format.


# In[15]:


d


# In[17]:


print(a.ndim)                  #ndim is used to print the dimensions of array.
print(b.ndim)
print(c.ndim)
print(d.ndim)


# # Conversion functions in numpy

# In[20]:


A=np.array([10,20,30,40,50])   #declared an array


# In[22]:


print(A)                       #printed the array


# In[25]:


res=np.asarray(A,dtype="float",order="C")    #applied asarray on the array.


# In[26]:


print(res)                      #returned array as a float dtype.


# In[28]:


B=np.array([[1,2,3],[4,5,6]])


# In[29]:


B


# In[30]:


res1=np.asarray(B,dtype="int",order="F")    #applied asarray on the array.


# In[33]:


print(res1)


# In[34]:


# to print all the elements in a single dimension we use nditer.
# as we are column major, we will get the following result.
for i in np.nditer(res1):
    print(i)


# In[35]:


res2=np.asarray(B,dtype="int",order="C")    #applied asarray on the array.


# In[36]:


# as we are row major, we will get the following result.
for i in np.nditer(res2):
    print(i)


# In[37]:


print(res2)


# In[38]:


s=b"hello welcome to python"   #b=bytes


# In[39]:


c=np.frombuffer(s,dtype="S1",count=-1,offset=0)  #frombuffer method.


# In[40]:


c


# In[41]:


c=np.frombuffer(s,dtype="S1",count=10,offset=0)


# In[42]:


c


# In[43]:


l=[10,20,30,40]


# In[44]:


d=np.fromiter(l,dtype="float",count=-1)   #fromiter method.
print(d)


# # arange,linspace,logspace.

# In[45]:


np.arange(0,10,2,dtype="int")  #arange.


# In[46]:


arr=np.arange(0,10,2,dtype="int")


# In[48]:


print(arr)


# In[53]:


arr=np.arange(0,10,dtype="float")


# In[54]:


arr


# In[51]:


arr1=np.linspace(0,10,5)     #linspace


# In[52]:


print(arr1)


# In[56]:


arr1=np.linspace(0,10,5,endpoint=False,retstep=True)    #retstep means it will return as tuple and with the difference.
print(arr1)


# In[57]:


arr2=np.logspace(0,10,num=4,endpoint=False,base=2)  #Logspace
print(arr2)


# # Shape,reshape,zeros,ones,full,eye

# In[58]:


x=[[10,20,30],[40,50,60]]  #by using shape we get the dimension of an array
np.shape(x)


# In[59]:


np.reshape(x,(3,2))  #by using reshape, we can change the shape of an array


# In[60]:


np.zeros((2,3)) # matrix of all the zeros


# In[61]:


np.ones((2,3)) #matrix of all the ones


# In[62]:


np.full((2,3),50)  #by using full, we will get a matrix of same element, which will be mentioned


# In[63]:


np.eye(3)  #diagonal elements will be one's and non diagonal elements wil be 0's.


# # Accessing and slicing

# In[64]:


p=np.array([10,20,30,40,50]) 


# In[65]:


print(p[0])  #accessing data by using index


# In[66]:


q=np.array([[10,20,30],[40,50,60]])  #2d array.


# In[67]:


q[0][1]             #accessing data from 2d array.


# In[68]:


q[0,1]


# In[69]:


q[1,2]


# In[71]:


r=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])


# In[72]:


r[0,1,1]  #accessing the data from 3d array


# In[73]:


v=np.array([10,20,30,40,50,60])   #slicing


# In[75]:


print(v)


# In[76]:


v[::]                              #slicing in 1d array


# In[77]:


v[:4]


# In[78]:


v[2:]


# In[79]:


v[1:3]


# In[81]:


u=np.array([[10,20,30],[40,50,60]])


# In[82]:


print(u)


# In[83]:


u[0,0:2]                            #slicing in 2d array


# In[84]:


u[1,0:2]


# In[86]:


w=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])


# In[87]:


w


# In[88]:


w[0,1,0:2]   #sliocing in 3d array


# # Axis

# In[96]:


#Axis=0 means we have to apply operations on column.
#Axis=1 means we have to apply operations on row.

f=np.array([[10,2,33],[4,50,6]])


# In[97]:


print(f)


# In[98]:


np.sort(f,axis=0)    #here axis=0, hence operation has been done on columns.


# In[99]:


np.sort(f,axis=1)   #here axis=1, hence operation has been done on rows.


# In[101]:



Data=np.array([[1, 2, 3],[4, 5, 6]])


# In[102]:


np.sum(Data,axis=1)     #sum of the elements of the first and second row.


# In[104]:


a=np.array([1,2,3,4,5,6,7,8,9,10])


# In[116]:


a*10


# In[117]:


a[::-1]


# In[119]:


a[::-1]


# In[120]:


a/2


# In[3]:


V=np.array([10,20,30],dtype="U")


# In[4]:


V


# In[30]:


V=np.asarray(V,dtype="int")


# In[31]:


V


# In[33]:


O=np.array([1,2,3,4])
P=np.array([5,6,7,8])
T=O/P
print(T)


# # Copy and View

# In[7]:


q=np.array([10,20,30,40])


# In[8]:


q


# In[9]:


w=q.copy()                        #In copy, external copy is created.


# In[10]:


w


# In[11]:


e=np.array([10,20,30,40])


# In[12]:


r=e.view()                         #In view, a reference is being created.


# In[13]:


r


# In[14]:


r[1]=44


# In[15]:


r


# # Concatenate

# In[22]:


C=np.arange(1,7).reshape(2,3)


# In[23]:


C


# In[24]:


X=np.arange(7,13).reshape(2,3)


# In[25]:


X


# In[28]:


np.concatenate((C,X))


# In[29]:


np.concatenate((C,X),axis=1)    #row wise concatenation


# In[34]:


C


# In[35]:


X


# In[38]:


np.stack((C,X))


# In[39]:


np.vstack((C,X))


# In[40]:


np.hstack((C,X))


# # Split

# In[44]:


G=np.arange(1,11)


# In[45]:


G


# In[46]:


np.split(G,2)


# In[48]:


np.array_split(G,3)


# # Searching

# In[49]:


j=np.arange(10,100,10)


# In[50]:


j


# In[53]:


np.where(j==30)                   #where returns the index of searched value in array.


# In[55]:


np.where(j%30==0)


# In[56]:


k=np.arange(10,100,10)


# In[57]:


k


# In[58]:


np.searchsorted(k,25)  #searched sorted will return the possible index for the value.


# # Sort

# In[65]:


n=np.array([[10,50,30],[50,80,60]])


# In[66]:


n


# In[67]:


np.sort(n)


# In[68]:


np.sort(n,axis=0)


# # Arithimetic operations

# In[69]:


m=np.array([1,2,3,4,5])
n=np.array([1,2,3,4,5])
z=np.add(m,n)


# In[70]:


z


# In[72]:


z=np.subtract(m,n)


# In[73]:


z


# In[74]:


z=np.multiply(m,n)


# In[75]:


z


# In[76]:


z=np.divide(m,n)


# In[77]:


z


# In[78]:


z=np.power(m,n)


# In[79]:


z


# In[80]:


z=np.mod(m,n)


# In[81]:


z


# In[82]:


zx=np.arange(1,11)


# In[83]:


zx


# In[84]:


zx*10


# # Statistical functions

# In[85]:


zz=np.arange(1,10).reshape(3,3)


# In[86]:


zz


# In[87]:


np.min(zz)


# In[89]:


np.max(zz)


# In[90]:


np.mean(zz)


# In[92]:


np.median(zz)


# In[93]:


np.std(zz)


# In[95]:


np.var(zz)


# In[ ]:



