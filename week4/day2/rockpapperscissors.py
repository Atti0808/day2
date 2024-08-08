import random
print("Welcome to the game ") 
print("Best of 7")


# player_score = 0
# computer_score = 0
# wins = 0


options = ( "rock", "paper","scissors",)
player = None
running = True

while running:
    player_score = 0
    computer_score = 0
   
    options = ( "rock", "paper","scissors",)
    player = None
    computer = random.choice(options)

    while player not in options:

        player = input("Enter a choice (rock,paper,scissors):").lower()

        print(f"Player :{player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("it`s a tie")
           
          
            

        elif player == "rock" and computer == "scissors" :
            print("You win!")
            player_score += 1
          

        elif player == "paper" and computer == "rock" :
            print("You win!")
            player_score += 1
         

        elif player == "scissors" and computer == "papper":
            print("You win!")
            player_score += 1
      


        else:
            print("You lose")
            computer_score += 1
           

     


print("your score" ,player_score)
print("computer score",computer_score)    
        # num1 = player_score
        # num2 = computer_score
        # wins = num1 + num2
        # print(wins)




