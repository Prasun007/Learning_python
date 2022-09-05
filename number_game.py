l1 = [5,6,2,3,4,9,8]
l1.sort()
l1.reverse()
print(l1)
# Number game starts from below. Difference between reverse() and reversed

def num_game():
    for i in reversed(range(0,9)): # or range(8,0,-1)
        num = int(input("Enter any number "))
        if num==18:
            print("Congrats you have guessed the hidden number in",i,"chances")
            break
        elif num>=20:
            print("Hidden no is less than", num)
            print("Chances left", i)
            if i==0:
                print("You Lost")
                break
        elif num<=15:
            print("Hidden no is more than", num)
            print("Chances left", i)
            if i==0:
                print("You Lost")
                break
        elif num<=10:
            print("Hidden no is more than", num)
            print("Chances left", i)
            if i==0:
                print("You Lost")
                break
        else:
            print("Hidden no is more than", num)
            print("Chances left", i)

num_game()

print("\n************Do you want to play again?************\n")

while(True):
    p = input("y for yes n for no ").lower()
    if p=="y":
        num_game()
        break
    elif p=="n":
        print("Thank you for playing")
        break
    else:
        print("wrong input")
        continue