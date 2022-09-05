def fun1():# Function created
    print("Inside function")

fun1()# Calling the function
fun1()
#print("Now",fun1()) #output None because nothing to return
"""
After creating function we must call the function
"""

def fun_2(a, b):# using variables with functions
    print("Inside fun_2 sum of a, b",a+b)
fun_2(5,5)
"""
Storing value of a function inside a variable and printing the variable
"""
def fun_2(a, b):# using variables with functions
    c=a+b
    print("Inside fun_2 sum of a, b",c)
    return c
var = fun_2(5,5)# Program execution starts from here. The program enters the def fun_2() with a=5, b=5 then adds and returns c then stores value in var.
print(var)

def fun_3(a, b):
    """This is a docstring and is used to write the purpose of the function"""
    average=(a+b)/2
    return average
v=fun_3(9, 6)
print(v)
print(fun_3.__doc__)# Prints docstring

def fun_3():
    """This is a docstring and is used to write the purpose of the function"""
    a=int(input("Enter "))
    b=int(input("enter "))
    average=(a+b)/2
    print(average)
    return average
v2=fun_3()
print("Average is", v2)

