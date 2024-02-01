# This is a sample Python script.
from datetime import date
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Account:
    min_amount = {"current":500, "saving":1000, "salary":2000}
    def __init__(self, acc_type, name, acc_number, creation_date, balance):
        self.acc_type = acc_type
        self.name = name
        self.acc_number = acc_number
        self.creation_date = creation_date
        self.balance = balance
        self.min_balance = Account.min_amount[acc_type]

    def __str__(self):
        return f"Type = {self.acc_type}\nName = {self.name}\nID = {self.acc_number}\nDate = {self.creation_date}\nBalance = {self.balance}"

def create_account(accounts):
    acc_type = input("Enter account type (e.g. current, savings, salary): ")
    name = input("Enter account holder's name: ")
    acc_number = input("Enter account number: ")
    print("Minimum",Account.min_amount[acc_type], "taka must be deposited to create the account")
    balance = float(input("Enter initial balance: "))

    new_account = Account(acc_type, name, acc_number, date.today(), balance)
    accounts.append(new_account)
    print("Account created successfully.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
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
        elif choice == 8:
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
