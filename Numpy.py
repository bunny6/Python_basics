#Array
import numpy as np    #importing the Numpy library. 'as' means Alternate name.

a=np.array([1,2,3])      #creating a array.
b=np.array(52)
print(a)                 #printing a array.
print(b)
type(a)                 #getting the data type.

c=np.array([[1,2,3],[4,5,6]])     #2d array. Matrix format.
c                      

d=np.array([[[1,2,3],[4,5,6]],[[7,8,6],[6,5,6]]])    #23 array. Matrix format.
d

print(a.ndim)                  #ndim is used to print the dimensions of array.
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Conversion functions in numpy
A=np.array([10,20,30,40,50])   #declared an array

print(A)                       #printed the array

res=np.asarray(A,dtype="float",order="C")    #applied asarray on the array.

print(res)                      #returned array as a float dtype.

B=np.array([[1,2,3],[4,5,6]])

B

res1=np.asarray(B,dtype="int",order="F")    #applied asarray on the array.

print(res1)

# to print all the elements in a single dimension we use nditer.
# as we are column major, we will get the following result.
for i in np.nditer(res1):
    print(i)

res2=np.asarray(B,dtype="int",order="C")    #applied asarray on the array.

# as we are row major, we will get the following result.
for i in np.nditer(res2):
    print(i)

print(res2)

s=b"hello welcome to python"   #b=bytes

c=np.frombuffer(s,dtype="S1",count=-1,offset=0)  #frombuffer method.

c

c=np.frombuffer(s,dtype="S1",count=10,offset=0)

c

l=[10,20,30,40]

d=np.fromiter(l,dtype="float",count=-1)   #fromiter method.
print(d)

#arange,linspace,logspace.
np.arange(0,10,2,dtype="int")  #arange.

arr=np.arange(0,10,2,dtype="int")

print(arr)

arr=np.arange(0,10,dtype="float")

arr

arr1=np.linspace(0,10,5)     #linspace

print(arr1)

arr1=np.linspace(0,10,5,endpoint=False,retstep=True)    #retstep means it will return as tuple and with the difference.
print(arr1)

arr2=np.logspace(0,10,num=4,endpoint=False,base=2)  #Logspace
print(arr2)

#Shape,reshape,zeros,ones,full,eye
x=[[10,20,30],[40,50,60]]  #by using shape we get the dimension of an array
np.shape(x)

np.reshape(x,(3,2))  #by using reshape, we can change the shape of an array

np.zeros((2,3)) # matrix of all the zeros

np.ones((2,3)) #matrix of all the ones

np.full((2,3),50)  #by using full, we will get a matrix of same element, which will be mentioned

np.eye(3)  #diagonal elements will be one's and non diagonal elements wil be 0's.

#Accessing and slicing

p=np.array([10,20,30,40,50]) 

print(p[0])  #accessing data by using index

q=np.array([[10,20,30],[40,50,60]])  #2d array.

q[0][1]             #accessing data from 2d array.

q[0,1]

q[1,2]

r=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])

r[0,1,1]  #accessing the data from 3d array

v=np.array([10,20,30,40,50,60])   #slicing

print(v)

v[::]                              #slicing in 1d array

v[:4]

v[2:]

v[1:3]

u=np.array([[10,20,30],[40,50,60]])

print(u)

u[0,0:2]                            #slicing in 2d array

u[1,0:2]

w=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])

w

w[0,1,0:2]   #sliocing in 3d array

#Axis

#Axis=0 means we have to apply operations on column.
#Axis=1 means we have to apply operations on row.

f=np.array([[10,2,33],[4,50,6]])

print(f)

np.sort(f,axis=0)    #here axis=0, hence operation has been done on columns.

np.sort(f,axis=1)   #here axis=1, hence operation has been done on rows.

Data=np.array([[1, 2, 3],[4, 5, 6]])

np.sum(Data,axis=1)     #sum of the elements of the first and second row.

a=np.array([1,2,3,4,5,6,7,8,9,10])

a*10

a[::-1]

a[::-1]

a/2

V=np.array([10,20,30],dtype="U")

V

V=np.asarray(V,dtype="int")

V

O=np.array([1,2,3,4])
P=np.array([5,6,7,8])
T=O/P
print(T)

#Copy and View

q=np.array([10,20,30,40])

q

w=q.copy()                        #In copy, external copy is created.

w

e=np.array([10,20,30,40])

r=e.view()                         #In view, a reference is being created.

r

r[1]=44

r

#Concatenate

C=np.arange(1,7).reshape(2,3)

C

X=np.arange(7,13).reshape(2,3)

X

np.concatenate((C,X))

np.concatenate((C,X),axis=1)    #row wise concatenation


# In[34]:

C

X

np.stack((C,X))

np.vstack((C,X))

np.hstack((C,X))

#Split

G=np.arange(1,11)

G

np.split(G,2)

np.array_split(G,3)

#Searching

j=np.arange(10,100,10)

j

np.where(j==30)                   #where returns the index of searched value in array.

np.where(j%30==0)

k=np.arange(10,100,10)

np.searchsorted(k,25)  #searched sorted will return the possible index for the value.

#Sort

n=np.array([[10,50,30],[50,80,60]])

n

np.sort(n)

np.sort(n,axis=0)


#Arithimetic operations

m=np.array([1,2,3,4,5])
n=np.array([1,2,3,4,5])
z=np.add(m,n)

z

z=np.subtract(m,n)

z

z=np.multiply(m,n)

z

z=np.divide(m,n)

z

z=np.power(m,n)

z

z=np.mod(m,n)

z

zx=np.arange(1,11)

zx

zx*10


#Statistical functions

zz=np.arange(1,10).reshape(3,3)

zz

np.min(zz)

np.max(zz)

np.mean(zz)

np.median(zz)

np.std(zz)

np.var(zz)







