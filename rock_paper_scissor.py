import random

def computer():
    options = ["Rock", "Paper", "Scissor"]
    comp_input = random.choice(options)
    return comp_input
i=0
while(i<10):
    user_input=input("Enter your choice ").upper()
    comp_input=computer()
    c_score=0
    u_score=0
    if user_input=='R' and comp_input=='Paper' or user_input=='P' and comp_input=='Scissor' or user_input=='S' and comp_input=='Rock':
        c_score = c_score + 1
        print(comp_input)
        print("Computer wins")
        print(f"{c_score} {u_score}")
        # for c_score in range(10):
        #     c_score+=1
        #     print(c_score)
        #     c_score+=1
        #     break
        i+=1

    elif user_input=='S' and comp_input=='Scissor' or user_input=='R' and comp_input=='Rock' or user_input=='P' and comp_input=='Paper':
         print(comp_input)
         print("Draw!")
         i+= 1
    elif user_input=='P' and comp_input=='Rock' or user_input=='S' and comp_input=='Paper' or user_input=='R' and comp_input=='Scissor':
        u_score += 1
        print(comp_input)
        print("User Won")
        print(f"{c_score} {u_score}")
        # for u_score in range(10):
        #     u_score+=1
        #     print(u_score)
        #     u_score+=1
        #     break
        i+=1

    else:
        print("Invalid input!")

