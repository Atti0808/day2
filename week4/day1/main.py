import random

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    max_games = 7
    user_score = 0
    computer_score = 0
    round_number = 0
    
    while round_number < max_games:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie this round!")
        
        round_number += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        print(f"Round {round_number}/{max_games} complete.\n")

    print("Game Over!")
    if user_score > computer_score:
        print(f"You are the overall winner with a score of {user_score} to {computer_score}!")
    elif user_score < computer_score:
        print(f"Computer is the overall winner with a score of {computer_score} to {user_score}!")
    else:
        print(f"The game is a tie with a score of {user_score} to {computer_score}.")

if __name__ == "__main__":
    main()
    