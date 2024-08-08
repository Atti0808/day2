# #atm
# am = input(int(500))
# acn = int(567128)

# def cash_dispense (am,acn):
#     print(f"withdrawing {am} from account number {acn}")

# pin = input("Please enter Pin Below")
# if input != 5678:
#     print ("Thank you ")

# else:
#      print("wrong")

# balance = 1000

# Define initial balance
balance = 1000

# Function to handle cash dispensing
def cash_dispense(amount, account_number):
    print(f"Withdrawing £{amount} from account number {account_number}")

# Prompt user for amount to withdraw
amount = int(input("Enter the amount you want to withdraw: "))

# Account number (in a real application, this would be handled securely)
account_number = 567128

# Prompt user for PIN
entered_pin = int(input("Please enter your PIN: "))

# Check if the entered PIN is correct
if entered_pin == 5678:
    # Check if there are sufficient funds
    if amount <= balance:
        cash_dispense(amount, account_number)
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: £{balance}")
    else:
        print("Insufficient funds.")
else:
    print("Incorrect PIN. Please try again.")




