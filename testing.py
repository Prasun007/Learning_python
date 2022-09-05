def f1():
    n1=int(input("Enter "))
    n2=int(input("Enter "))
    n3=n1+n2
    print(n3)
    again()
def again():
    inp=input("Want again? ")
    if inp == "yes":
        f1()
    elif inp == "no":
        print("Ok")
    else:
        again()
f1()
