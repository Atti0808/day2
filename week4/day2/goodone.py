import random

print("Rock, Paper and Scissors ")
print("Best of 7")

options = (" rock", " paper", " scissors")
running = True

while running:


    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Chose one of the 3 (rock , paper , scissors): ")
    print(f" player:{player} ")
    print(f" computer:{computer}")

    if player == computer :
        print("It`s a Tie")
    elif player == "rock" and computer == "scissors" :
        print("You Win!")
    elif player == "paper" and computer == "rock" :
        print("You Win!")
    elif player == "scissors" and computer == "paper" :
        print("You Win!")
    else:
        print("You lose")
print("Your Score ")        

