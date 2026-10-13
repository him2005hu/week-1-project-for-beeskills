# Mini Project: Simple ATM Simulator

# Account details
correct_pin = "2005"
balance = 50000.0


# Function 1: User Login
def login():
    print("===== Welcome to Simple ATM =====")

    for attempt in range(3):
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("\nLogin Successful!")
            return True
        else:
            print("Incorrect PIN! Try again.")

    print("\nToo many incorrect attempts. Access denied.")
    return False


# Function 2: Check Balance
def check_balance():
    print(f"\nYour current balance is: Rs. {balance:.2f}")


# Function 3: Deposit Money
def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: Rs. "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print(f"Updated balance: Rs. {balance:.2f}")
        else:
            print("Please enter an amount greater than zero.")

    except ValueError:
        print("Invalid amount! Please enter a number.")


# Function 4: Withdraw Money
def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: Rs. "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            print("Please collect your cash.")
            print(f"Remaining balance: Rs. {balance:.2f}")

    except ValueError:
        print("Invalid amount! Please enter a number.")


# Main ATM Program
def atm_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


# Main Execution
if login():
    atm_menu()
else:
    print("Please contact your bank for assistance.")