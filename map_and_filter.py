v=lambda a:a%2  #lambda function is a one line function. It is use ful when we have to use a function only once in a program.

v(2)

v(19)

list=[1,2,3,4,5,6]
v=lambda a:a%2

r=v(5)

print(r)

def sum(a,b):
    return a+b

sum(2,4)

r=lambda a,b:a+b

r(2,4)

list2=[1,2,3,4,5,6,7]

t=list(filter(lambda a:a%2==0,list2))

y=list(map(lambda n:n+2,list2))

print(y)

num=[1,2,3,4,5,6,7]

from random import shuffle

shuffle(num)

print(num)

num=[1,2,3,4,5,6,7]
evens=list(filter(lambda n : n%2==0,num))
print(evens)

listt=[1,2,3,4,5,6]
f=list(filter(lambda n:n%3==0,listt))

print(f)







