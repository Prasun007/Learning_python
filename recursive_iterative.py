# def factorial(n):
#     fac=1
#     for i in range(n):
#         fac=fac*(i+1)
#     return fac
# number=int(input("Enter "))
# print(factorial(number))
def factorial(n):
   if n==1:
       return 1
   else:
       return n*factorial(n-1)
print(factorial(6))
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))
for i in range(6):
    print(fib(i))