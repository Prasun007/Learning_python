num1 = input("Enter a number ")
num2 = input("Enter another number ")
print(int(num1)+int(num2))
print("This portion is very important")
l1=[num1, num2]
for i in l1:
    print(i)

num3 =input("Enter a number ")
num4 =input("Enter another number ")
try:
    print(int(num3)+int(num4))
except Exception as e:
    print(e)
print("This portion is very important")
l2=[num3, num4]
for i in l2:
    print(i)
