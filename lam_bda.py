l=[[1,2],[15,31],[10,9]]
l.sort(key=lambda x:x[0])
print(l)

add=lambda a, b: a+b
a=int(input("Enter a "))
b=int(input("Enter b "))
print(add(a,b))

def a_first(a):
    return a[1]

l=[[1,20],[15,5],[10,9]]
l.sort(key=a_first)# key takes argument as a function.
print(l)