import random
def stone_paper_scissors():
    x=["stone","paper","scissors"]
    print("Welcome to the mini game....")
    print("type exit if you want to quit the game")
    while True:
        try:
            user_choice=input("enter your choice : ").lower()
            if (user_choice=="exit"):
                print("thanks for playing...")
                break
            if(user_choice not in x):
                raise Exception("enter correct choice and try again")
            
            computer_choice = random.choice(x)
            print(f"Computer chose: {computer_choice}")
             
            
            if user_choice == computer_choice:
                print("its a tie...")


            elif (user_choice == "stone" and computer_choice == "scissor") or(user_choice == "paper" and computer_choice == "stone") or (user_choice == "scissors" and computer_choice == "paper"):
                print("You won ......")
            
            else:
                print("Computer won.....")
        except BaseException as e:
            print("exception name is ",e)
stone_paper_scissors()
