import random

def roll_dice():
    """Simulates rolling a six-sided dice and returns the result."""
    return random.randint(1, 6)

def dice_roll_game(target_score=40):
    """Runs a dice roll game until the player's score reaches the target score."""
    score = 0
    rounds = 0

    print(f"Welcome to the Dice Roll Game! Reach a score of {target_score} to win.")

    while score < target_score:
        # Roll the dice
        result = roll_dice()
        rounds += 1
        score += result

        # Print the result of the roll and the current score
        print(f"Round {rounds}: You rolled a {result}. Current score: {score}")

        if score >= target_score:
            print(f"Congratulations! You reached the target score of {target_score} in {rounds} rounds.")
            break

    print("Game over! Thank you for playing!")

# Run the dice roll game
if __name__ == "__main__":
    dice_roll_game()

