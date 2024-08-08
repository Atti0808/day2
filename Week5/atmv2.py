# Constants
ACCOUNT_NUMBER = 567128
CORRECT_PIN = 5678
INITIAL_BALANCE = 1000

# Function to handle cash dispensing
def cash_dispense(amount, account_number):
    print(f"Withdrawing £{amount} from account number {account_number}")

# Main function to handle the ATM operations
def atm_operations():
    balance = INITIAL_BALANCE

    # Prompt user for amount to withdraw
    while True:
        try:
            amount = int(input("Enter the amount you want to withdraw: £"))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Prompt user for PIN
    while True:
        try:
            entered_pin = int(input("Please enter your PIN: "))
            if entered_pin == CORRECT_PIN:
                break
            else:
                print("Incorrect PIN. Please try again.") #message prompt if user entered incorrect pin
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Process the withdrawal
    if amount <= balance:
        cash_dispense(amount, ACCOUNT_NUMBER)
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: £{balance}")
    else:
        print("Insufficient funds.") # in case there are insufficient funds

# Run the ATM operations
if __name__ == "__main__":
    atm_operations()
