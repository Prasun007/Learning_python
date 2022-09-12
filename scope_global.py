"""
Error because x=10 is global we cannot change x inside function
"""

# x=10
# def fun():
#     x+=5
#     print(x)
# fun()
"""
To change x use global keyword
"""
x=10
def fun():
    global x
    x+=5
    print(x)
fun()
x=40
def f_1():
    x=20
    def f_2():
        global x
        x=30
    print("Before calling f_2()"+"x="+str(x))
    f_2()
    print("After calling f_2() x = ",x)# Edike x change hy na karon global use korle ida shob functiion thkya bair hoia jay naki ekta nested function upor check kore

f_1()
print(x)#x=30 globally changed
def f_3():
    global x
    x+=2
    print(x)
f_3()