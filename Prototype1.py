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
    print("Processing...")
    time.sleep(2)
    print(f"! Income added successfully: {description} - ₱ {amount}")

def add_expense(description, amount):
    transaction = {
        'date': datetime.datetime.now(),
        'description': description,
        'amount': -amount,
        'type': 'expense'
    }
    transactions.append(transaction)
    print("Processing...")
    time.sleep(2)
    print(f"! Expense added: {description} - ₱ {amount}")

def view_balance():
    print("Calculating Balance. Please Wait...")
    time.sleep(2)
    balance = sum(transaction['amount'] for transaction in transactions)
    print(f"[Current balance: ₱ {balance:.2f} ]")

def view_transactions():
    print("Fetching Data....")
    time.sleep(3)
    if len(transactions) == 0:
        print("="*34,"[No transaction record.]","="*34)
    else:
        print("="*38,"Transaction History","="*38)
        for i, (transaction) in enumerate(transactions):
            date = transaction['date'].strftime('Date: %Y-%m-%d - Time: %H:%M:%S')
            description = transaction['description']
            amount = transaction['amount']
            type_ = transaction['type']
            print(f"{i+1}. {date} - Description: {description} - Type: {type_} - Amount: ₱ {amount:.2f}")

def clear_transaction_history():
    if len(transactions) == 0:
        print("No transaction to delete.")
    else:
        print("=" * 38, "Transaction History", "=" * 38)
        for i, (transaction) in enumerate(transactions):
            date = transaction['date'].strftime('Date: %Y-%m-%d - Time: %H:%M:%S')
            description = transaction['description']
            amount = transaction['amount']
            type_ = transaction['type']
            print(f"{i + 1}. {date} - Description: {description} - Type: {type_} - Amount: ₱ {amount:.2f}")

        print()
        choice = int(input("Enter the transaction number to delete: "))

        if 0 < choice <= len(transactions):
            del transactions[choice - 1]
            print("Processing...")
            time.sleep(2)
            print("Account Deleted.")
        else:
            print("Invalid Account Number.")

def main():
    while True:
        print("\n==[ Expense Tracker in Python ]==")
        print('1. Add income')
        print('2. Add expense')
        print('3. View balance')
        print('4. View transaction')
        print('5. Clear Transaction History')
        print('6. Exit')
        choice = input("= Choose an option (1-6):  ")
        print()
        if choice == '1':
            print("[Income Descriptions: Salary, Investment, Bonus, Part-time, etc...]")
            while True:
                description = input("Enter Income Description: ")
                if description.isalpha():
                    while True:
                        try:
                            amount = float(input("Enter Income Amount: ₱ "))
                            if amount <= 0:
                                print("Amount should not be below zero")
                                continue
                            else:
                                add_income(description, amount)
                                break  # Exit the inner loop if input is valid
                        except ValueError:
                            print("Invalid input: Please enter a number.")
                    break  # Exit the outer loop if both inputs are valid
                else:
                    print("Invalid input: Description should be a string.")

        elif choice == '2':
            print("Expense Category: food, transportation, bills etc..., ")
            while True:
                description = input("Enter Expense Category: ")
                if description.isalpha():
                    while True:
                        try:
                            amount = float(input("Enter Expense Amount: ₱ "))
                            add_expense(description, amount)
                            break  # Exit the inner loop if input is valid
                        except ValueError:
                            print("Invalid input: Please enter a number.")
                    break  # Exit the outer loop if both inputs are valid
                else:
                    print("Invalid input: Description should be a string.")
        elif choice == '3':
            view_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            clear_transaction_history()
        elif choice == '6':
            print("Exiting...Thank you for using this app :)")
            time.sleep(3)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

