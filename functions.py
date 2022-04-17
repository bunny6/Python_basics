#we define a function using a keyword def
def fun(name):
    print('hello'+name)



fun('good')

#defining a addition function
def add_fun(num1,num2):
    return num1+num2

result=add_fun(1,2)

result


def say_hello(name):
    print("hello {}".format(name))


say_hello('Huh')

def shu(name="default"):
    return(name)


re=shu()

re


#login functions

2 % 2 == 0


#mod returns the remainder

2 % 3

20 % 2 == 0

def check_list(num_list):
    for i in num_list:
        if i%2==0:
            return True
        else:
            pass
    return False    


check_list([1,2,3])

check_list([1,1,1])

type(check_list)

#Now instead of returning boolean value, we will return the actual value

def check_list(new_list):
    
    even_number=[]
    
    for i in new_list:
        if i%2==0:
            even_number.append(i)
        else:
            pass
        
    return even_number    

check_list([1,2,3])

check_list([2,3,4])


#Tuples

s_p=[('App',200),('Sam',200),('Web',300)]

for i in s_p:
    print(i)

for i,j in s_p:
    print(i)

for i,j in s_p:
    print(j)

work_hours=[('App',200),('Sam',200),('Web',300)]

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

li=['dileep','shubham']

lis=[]
for i in li:
    print(i[3])

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

employee_check(work_hours)

def even(num):
    
    even_num=[]
    
    for i in num:
        if i%2==0:
            even_num.append(i) 
        else:
            pass
    return even_num    

even([1,2,3,4,5])


def cube(num):
    cube=[]
    for i in num:
        if i%3==0:
            cube.append(i)
        else:
            pass
        
    return cube


cube([1,3,6,9,8])






