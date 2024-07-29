class BankAccount:
    def __init__(my, account_number, initial_balance=0):
        account_number=int(input("Enter a account number"))
        my.account_number = account_number
        my.balance = initial_balance

    def deposit(self, amount):
        my.balance += amount
        return my.balance

    def withdraw(my, amount):
        if amount > my.balance:
            raise ValueError("Insufficient funds")
        my.balance -= amount
        return my.balance

    def get_balance(my):
        return my.balance

    def __str__(my):
        return f"Account {my.account_number}: Balance = {my.balance:.2f}"
