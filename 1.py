with open("demo.txt", "r+") as f:
    print(f.read())
    while(True):
        b=input("y or n")
        if b=='y':
            a=input("Write ")
            f.write(a)
            print(f.read())
            continue
        elif b=='n':
            break
        else:
            print("Invalid")
            continue
with open("demo.txt") as f:
    print(f.read())
