import time
import datetime

account = []
expenses = []

def add_account():
    account.append((names,amount))

names = input("Name: ")
amount = float(input("Amount: ₱ "))
print("Processing...")
time.sleep(3)
print("Account added successfully!")


def view_account():
    if len(account) == 0:
        print("No account was currently added.")
    else:
        print("List of accounts:")
        for i, (names, amount) in enumerate(account):
            print(f"{i+1}. Name: {names} | Balance: ₱ {amount}")



def delete_account():
    if len(account) == 0:
        print("No account to delete.")
    else:
        print("List of accounts:")
        for i, (names, amount) in enumerate(account):
            print(f"{i+1}. Name: {names} | Balance: ₱ {amount}")
        choice = int(input("Enter the account number to delete: "))

        if 0 < choice <= len(account):
            del account[choice-1]
            print("Account Deleted.")
        else:
            print("Invalid Account Number.")



def add_expenses():
    expenses.append((expense, cost))

print("Add expense: [shopping, food, transportation, bills etc...]")
expense = input("Expense: ")
cost = float(input("Cost: ₱ "))
print("Processing...")
time.sleep(3)
print("Expenses added successfully!")


def view_expenses():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    if len(expenses) == 0:
        print("No expense was currently added.")
    else:
        print("List of expenses:")
        for i, (expense, cost) in enumerate(expenses):
            print(f"{i+1}. Date: {formatted_date} | Expense: {expense} | Cost: ₱ {cost} | Balance left: {cost-amount}")



def delete_expenses():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    if len(expenses) == 0:
        print("No Expenses to delete.")
    else:
        print("List of Expenses:")
        for i, (expense, cost) in enumerate(expenses):
            print(f"{i + 1}. Date: {formatted_date} | Expense: {expense} | Cost: ₱ {cost} | Balance left: {cost - amount}")
        choice = int(input("Enter the Expense number to delete: "))

        if 0 < choice <= len(expenses):
            del expenses[choice-1]
            print("Expense Deleted.")
        else:
            print("Invalid Number.")


def main():
    while True:
        print("==[ Hi! Welcome to our Expense Tracker Project made in Python. ]==")
        print("1. Add Account")
        print("2. View Account")
        print("3. Delete Account")
        print("4. Add Expenses")
        print("5. View Expenses")
        print("6. Delete Expenses")
        print("7. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_account()
        elif choice == 2:
            view_account()
        elif choice == 3:
            delete_account()
        elif choice == 4:
            add_expenses()
        elif choice == 5:
            view_expenses()
        elif choice == 6:
            delete_expenses()
        elif choice == 7:
            break
        else:
            print("Invalid Input, Please try again.")

if __name__ == "__main__":
    main()
