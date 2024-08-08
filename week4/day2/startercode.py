import random

options = ("rock", "paper","scissors")
running = True

while running :

    You_Chose = None
    Computer = random.choice(options)

    while You_Chose not in options:
        You_Chose = input("Please select one (rock , paper , scissors): ")

    print(f"You Chose: {You_Chose}")
    print(f"Computer Chose: {Computer}")

    if You_Chose == Computer:
        print("It`s Draw")
    elif You_Chose == "rock" and Computer == "scissors":
        print("You Win!")
    elif You_Chose == "paper" and Computer == "rock":
        print("You Win!")
    elif You_Chose == "scissors" and Computer == "paper":
        print("You Win!")
    else:
        print("You lose!")    

    play_again = input("Do you want to play again? (yes/no):").lower()
    if play_again!= "yes":
        print("Thanks for playing!")
        break

                       
    



   

