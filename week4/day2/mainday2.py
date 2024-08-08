import random

options = ( "rock", "paper","scissors",)
player = None
computer = random.choice(options)
running = True

print("Welcome to the game ") 
print("Best of 7")

player_score = 0
computer_score = 0
rounds = 0

options = ( "rock", "paper","scissors",)
player = None
computer = random.choice(options)
running = True

# print("Welcome to the game ") 
# print("Best of 7")

while running :
    while player not in options:
        player("Enter a choice(rock, paper, scissors):")

    print(f"Player: {player}")
    print(f"Computer: {computer}")    

    if player == computer:
        print("It`s Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose")
print("your score" ,player_score)
print("computer score",computer_score)
rounds = (player_score + computer_score)        

    

