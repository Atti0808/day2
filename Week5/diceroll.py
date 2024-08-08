import random

def roll_dice():
    """Simulates rolling a six-sided dice and returns the result."""
    return random.randint(1, 6)

def dice_roll_game():
    """Runs a simple dice roll game."""
    print("Welcome to the Dice Roll Game!")
    
    while True:
        # Ask the user if they want to roll the dice
        user_input = input("Type 'y' to roll the dice or 'n' to exit: ").strip().lower()
        
        if user_input == 'y':
            # Roll the dice and display the result
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif user_input == 'n':
            # Exit the game
            print("Thank you for playing! Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid input. Please type 'roll' or 'quit'.")

# Run the dice roll game
if __name__ == "__main__":
    dice_roll_game()
