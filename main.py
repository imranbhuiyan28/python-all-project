

def atm():
    balance_input = input('Enter your initial balance (or press Enter for 0): ')
    if balance_input.isdigit():
        balance = float(balance_input)
    else:
        balance = 0
    print('welcome to ATM service')


    while True:
        print(f"You have total balance: {balance}")

        user = input('Enter W to withdraw, D to deposit, S to show balance, or END to exit: ').lower()
        if user == 'end':
            print("thank for using our ATM. Good Bye")
            break
        elif user == 'w':
            balance = withdraw(balance)
        elif user == 'd':
           balance = deposit(balance)
        elif user == 's':
            show_balance(balance)
        else:
            print('Invalid option, please enter again.')


# withdraw function
def withdraw(balance):
    user_input = input("Enter the withdraw balance: ")
    if user_input.isdigit():
        withdraw_balance = float(user_input)
        if withdraw_balance > balance:
            print("Insufficient funds! ")
        elif withdraw_balance < 0:
            print("invalid digit")
        else:
            balance -= withdraw_balance
    else:
        print(" print('Invalid number, please enter again.')")

    return balance



#deposit function
def deposit(balance):
    user_input = input("Enter the deposit balance: ")
    if user_input.isdigit():
        deposit_balance = float(user_input)
        if deposit_balance <= 0:
            print("'Invalid amount! Please enter a valid amount.' ")
        else:
            balance += deposit_balance
    else:
        print(" print('Invalid number, please enter again.')")
    return balance



#show balance
def show_balance(balance):
    print(f"Your total balance is: {balance}")





atm()
