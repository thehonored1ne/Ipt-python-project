import datetime
import time

transactions = []

def add_income(description, amount):
    transaction = {
        'date': datetime.datetime.now(),
        'description': description,
        'amount': amount,
        'type': 'income'
    }
    transactions.append(transaction)
    print(f"Income added: {description} - {amount}")

def add_expense(description, amount):
    transaction = {
        'date': datetime.datetime.now(),
        'description': description,
        'amount': -amount,
        'type': 'expense'
    }
    transactions.append(transaction)
    print(f"Expense added: {description} - {amount}")

def view_balance():
    balance = sum(transaction['amount'] for transaction in transactions)
    print(f"Current balance: ₱ {balance:.2f}")

def view_transactions():
    for transaction in transactions:
        date = transaction['date'].strftime('%Y-%m-%d %H:%M:%S')
        description = transaction['description']
        amount = transaction['amount']
        type_ = transaction['type']
        print(f"{date} | {description} | {type_} | ₱ {amount:.2f}")

def main():
    while True:
        print("\nIncome Tracker in Python")
        print('1. Add income')
        print('2. Add expense')
        print('3. View balance')
        print('4. View transaction')
        print('5. Exit')
        choice = input("choose an option: ")

        if choice == '1':
            description = input('enter income description: ')
            amount = float(input('enter income amount: '))
            add_income(description, amount)
        elif choice == '2':
            description = input('enter expense description: ')
            amount = float(input('enter expense amount: '))
            add_expense(description, amount)
        elif choice == '3':
            view_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

