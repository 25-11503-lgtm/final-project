# Sample account information for classroom demonstration.
ACCOUNT_NAME = "Student Account"
STARTING_BALANCE = 1500.00
DEFAULT_PIN = "1234"
MAX_PIN_ATTEMPTS = 3


def authenticate(correct_pin, max_attempts):
    """Ask for a PIN and return True if the user enters it correctly."""
    attempts = 0
    while attempts < max_attempts:
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == correct_pin:
            print(f"\nWelcome, {ACCOUNT_NAME}!")
            return True
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
        else:
            print("Too many incorrect attempts. Your session is locked.")
    return False


def read_amount(prompt):
    """Read a positive amount and return it as a float."""
    while True:
        raw_amount = input(prompt).strip()
        try:
            amount = float(raw_amount)
            # Reject zero, negative amounts, and values with more than 2 decimals.
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
            elif round(amount, 2) != amount:
                print("Please enter an amount with no more than 2 decimal places.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Invalid amount. Enter numbers only (example: 250 or 250.50).")


def show_balance(balance):
    """Display and return the current account balance."""
    print("\n--- BALANCE INQUIRY ---")
    print(f"Available balance: PHP {balance:,.2f}")
    return balance


def deposit(balance, history):
    """Add a valid deposit to the balance and record the transaction."""
    print("\n--- CASH DEPOSIT ---")
    amount = read_amount("Enter deposit amount (PHP): ")
    balance += amount
    history.append(("Deposit", amount, balance))
    print(f"Deposit successful: PHP {amount:,.2f}")
    print(f"New balance: PHP {balance:,.2f}")
    return balance


def withdraw(balance, history):
    """Withdraw money only when the requested amount is within the balance."""
    print("\n--- CASH WITHDRAWAL ---")
    amount = read_amount("Enter withdrawal amount (PHP): ")

    # Both conditions must be true: enough funds and a valid positive amount.
    if amount <= balance and amount > 0:
        balance -= amount
        balance = round(balance, 2)
        history.append(("Withdrawal", amount, balance))
        print(f"Please take your cash: PHP {amount:,.2f}")
        print(f"Remaining balance: PHP {balance:,.2f}")
    elif amount > balance:
        print("Transaction declined: insufficient funds.")
        print(f"Your current balance is PHP {balance:,.2f}.")
    else:
        print("Transaction declined: invalid amount.")
    return balance


def show_history(history):
    """Print all completed transactions using a for loop."""
    print("\n--- TRANSACTION HISTORY ---")
    if len(history) == 0:
        print("No completed transactions in this session.")
    else:
         for number, transaction in enumerate(history, start=1):
            transaction_type, amount, balance_after = transaction
            print(
                f"{number}. {transaction_type}: PHP {amount:,.2f} "
                f"| Balance after: PHP {balance_after:,.2f}"
            )
    return len(history)


def display_menu():
    """Print the main menu and return the user's menu selection."""
    print("\n========== SIMPLE ATM ==========")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    return input("Choose an option (1-5): ").strip()


def run_atm():
    """Control authentication and repeat the menu until the user exits."""
    balance = STARTING_BALANCE
    pin = DEFAULT_PIN
    history = []

    print("================================")
    print("       SIMPLE ATM SIMULATOR     ")
    print("================================")
    print(f"Account: {ACCOUNT_NAME}")
    print("Demo note: use the sample PIN 1234.")

    if not authenticate(pin, MAX_PIN_ATTEMPTS):
        return

    running = True
    while running:
        choice = display_menu()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance, history)
        elif choice == "3":
            balance = withdraw(balance, history)
        elif choice == "4":
            count = show_history(history)
            print(f"Total completed transaction(s): {count}")
        elif choice == "5":
            print("\nThank you for using the Simple ATM Simulator.")
            print(f"Final balance: PHP {balance:,.2f}")
            running = False
        else:
            # This branch handles text, blank entries, and numbers outside 1-5.
            print("Invalid menu choice. Please enter a number from 1 to 5.")

    print("Session ended.")


if __name__ == "__main__":
    run_atm()
