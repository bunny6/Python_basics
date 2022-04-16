a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
try:                                            #in try block we write the instructions in which we expect the exception.
    c=a/b
    print(c)
except:                                         #in except block we handle the instructions which raise the exception.
    print("Exception raised")
else:
    print("No exception")
finally:
    print("Program ends")

a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
try:
    c=a/b
    print(c)
except:
    print("Exception raised")
else:
    print("No exception")
finally:
    print("Program ends")

#Single exception
a=int(input("Enter value of A:"))
b=int(input("Enter value of B:"))

try:
    c=a/b
    print(c)
except Exception as e:
    print(e)
    






