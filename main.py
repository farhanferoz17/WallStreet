# This is a sample Python script.
from datetime import date
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Account:
    min_amount = {"current":500, "savings":1000, "salary":2000}
    def __init__(self, acc_type, name, acc_number, creation_date, balance):
        self.acc_type = acc_type
        self.name = name
        self.acc_number = acc_number
        self.creation_date = creation_date
        self.balance = balance
        self.min_balance = Account.min_amount[acc_type]

    def __str__(self):
        return f"Name = {self.name}\nID = {self.acc_number}\nType = {self.acc_type}\nCreated on {self.creation_date}\nBalance = {self.balance}"

def create_account(accounts):
    acc_type = input("Enter account type (e.g. current, savings, salary): ")
    name = input("Enter account holder's name: ")
    while True:
        acc_number = input("Enter account number: ")
        if not search_account(accounts, acc_number, False):
            break
        else:
            print("Account number already exists, try again!")
    print("Minimum",Account.min_amount[acc_type], "taka must be deposited to create the account")
    balance = float(input("Enter initial balance: "))

    new_account = Account(acc_type, name, acc_number, date.today(), balance)
    accounts.append(new_account)
    print("Account created successfully.")

def display_accounts(accounts):
    for account in accounts:
        print(account)

def update_account(accounts):
    acc_number = input("Enter the account number to update: ")
    for account in accounts:
        if account.acc_number == acc_number:
            account.name = input("Enter new account holder's name: ")
            print("Account updated successfully.")
            return

    print("Account not found.")

def delete_account(accounts):
    acc_number = input("Enter the account number to delete: ")
    for account in accounts:
        if account.acc_number == acc_number:
            accounts.remove(account)
            print("Account deleted successfully.")
            return
    print("Account Not Found.")

def deposit(accounts):
    acc_number = input("Enter the account number for deposit: ")
    for account in accounts:
        if account.acc_number == acc_number:
            amnt = float(input("Enter deposit amount: "))
            account.balance += amnt
            print("Deposit successful.")
            return
    print("Account Not Found.")

def withdraw(accounts):
    acc_number = input("Enter the account number for withdrawal: ")
    for account in accounts:
        if account.acc_number == acc_number:
            amnt = float(input("Enter withdrawal amount: "))
            if account.balance - amnt >= Account.min_amount[account.acc_type]:
                account.balance -= amnt
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
            return
    print("Account Not Found.")

def search_account(accounts, acc_number, prnt):
    for account in accounts:
        if account.acc_number == acc_number:
            if prnt:
                print(account)
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    accounts = []

    while True:
        print("Banking Application Menu:")
        print("1. Create a new account")
        print("2. Display all accounts")
        print("3. Update an account")
        print("4. Delete an account")
        print("5. Deposit and amount into your account")
        print("6. Withdraw an amount from your account")
        print("7. Search for account")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            create_account(accounts)
        elif choice == 2:
            display_accounts(accounts)
        elif choice == 3:
            update_account(accounts)
        elif choice == 4:
            delete_account(accounts)
        elif choice == 5:
            deposit(accounts)
        elif choice == 6:
            withdraw(accounts)
        elif choice == 7:
            acc_num = input("Enter account number to search:")
            foundflag = search_account(accounts, acc_num, True)
            if foundflag:
                print("Account Found.")
            else:
                print("Account Not Found.")
        elif choice == 8:
            print("Exiting Banking Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 8.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
