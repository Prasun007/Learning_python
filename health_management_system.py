def getdatetime():
    import datetime
    return datetime.datetime.now()

def doc_prasun():
    var = int(input("1 to update Diet Chart\n2 to update Exercises "))
    if var==1:
        with open("prasun.txt", "r+") as f1:
            print(f1.read())
            while(True):
                p_u=input("Update Diet Chart\n")
                f1.write("\n" + str(getdatetime()) + " " + p_u)
                n=input("q to quit u to update more ")
                if n=='q':
                    break
                elif n=='u':
                    continue
    elif var==2:
        with open("prasun_exercise.txt", "r+") as f2:
            print(f2.read())
            while(True):
                p_u=input("Update Exercises\n")
                f2.write("\n" + str(getdatetime()) + " " + p_u)
                n=input("q to quit u to update more ")
                if n=='q':
                    break
                elif n=='u':
                    continue

    with open("prasun.txt") as f:
        print(f.read())
    with open("prasun_exercise.txt") as f2:
        print(f2.read())

def doctor():
    while(True):
        pass_wrd = input("Please enter password to proceed ")
        if pass_wrd=="Prasun007":
            break
        else:
            print("Invalid")
            continue

    print("Which patients file do you want to access? ")
    print(" 1. Prasun\n 2. Harry\n 3. Rohan")

    p_acc = int(input())
    print("Do you want to access\n 1. Diet Chart\n 2. Exercises ")
    p_acc2 = int(input())
    if p_acc==1 and p_acc2==1:
        p1 = open("prasun.txt")
        content = p1.read()
        print(content)
        p1.close()
        while (True):
            r_inp = int(input("Enter 1 for Diet Chart 2 for Exercises q to quit").lower())# typecasted to int therefore .lower() works inside because it is method of string
            if r_inp==1:
                with open("prasun.txt") as f1:
                    print(f1.read())
                    #continue
                up=input("Do you want to update this patients Diet Chart/Exercises y/n? ").lower()
                if up=='y':
                    doc_prasun()
                else:
                    continue
            elif r_inp==2:
                with open("prasun_exercise.txt") as f2:
                    print(f2.read())
                    continue
            elif str(r_inp)=="q":
                break
            else:
                print("Invalid Input")
                continue
    elif p_acc==1 and p_acc2==2:
        p1 = open("prasun_exercise.txt")
        content = p1.read()
        print(content)
        p1.close()


doctor()
