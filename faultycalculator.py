#45*3=555, 56+9=77, 56/6=4 # These operations are faulty exceprt these are correct
num1 = int(input("Enter 1st number "))
print("Select the operator from '*' '+' '/' ")
op = input()
num2 = int(input("Enter second number "))
if (num1==45) & (op=='*') & (num2==3):
    print(555)
elif (num1==56) & (op=='+') & (num2==9):
    print(77)
elif (num1==56) & (op=='/') & (num2==6):
    print(4)
elif op=='*':
    print(num1*num2)
elif op=='+':
    print(num1+num2)
else:
    print(num1/num2)
