# Define user ID and password
user_id = "vs_kengam"
password = "vs@4444"

def main():
    # Prompt user for credentials
    customer_name = input("Enter Your User ID:")
    customer_password = input("Enter Your Password:")

    # Authenticate user
    if customer_name == user_id and customer_password == password:
        print_menu()
    else:
        print("Please enter valid user ID or Password")

def print_menu():
    # Display menu options
    print('''
    1. Check Balance
    2. Cash Deposit
    3. Cash Withdrawal
    4. Exit
    ''')

    # Initialize balance
    available_balance = 20000

    # Prompt user for choice
    option = int(input("Select Your Choice:"))

    # Process user choice
    if option == 1:
        check_balance(available_balance)
    elif option == 2:
        deposit_cash(available_balance)
    elif option == 3:
        withdraw_cash(available_balance)
    elif option == 4:
        print("Thank you for Banking with us. Have a great day!")
    else:
        print("Invalid option. Please select a valid option.")

def check_balance(balance):
    # Display available balance
    print("Available Balance:", balance)

def deposit_cash(balance):
    # Prompt user for deposit amount
    deposit_amount = int(input("Enter the amount you want to deposit:"))
    # Update balance
    balance += deposit_amount
    print("New Balance after Deposit:", balance)

def withdraw_cash(balance):
    # Prompt user for withdrawal amount
    withdrawal_amount = int(input("Enter the amount you want to withdraw:"))
    # Check if withdrawal amount exceeds balance
    if withdrawal_amount > balance:
        print("Insufficient balance.")
    else:
        # Update balance
        balance -= withdrawal_amount
        print("New Balance after Withdrawal:", balance)

if __name__ == "__main__":
    main()
