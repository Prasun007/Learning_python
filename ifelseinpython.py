var1 = 6
var2 = 56
var3 = int(input("Enter number "))

if var3>var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:                 # Note to self: No conditions required in else
    print("Less")

list=[5, 7, 3]
print(5 in list)
print(5 not in list)

if 5 in list:
    print("5 present")
