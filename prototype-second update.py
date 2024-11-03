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
    print("\033[32mProcessing... \033[0m")
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
    print("\033[32mProcessing... \033[0m")
    time.sleep(2)
    print(f"! Expense added: {description} - ₱ {amount}")

def view_balance():
    print("\033[92mVIEW BALANCE\033[0m")
    print("\033[32mCalculating Balance. Please Wait...\033[0m")
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
            print("Transaction Deleted.")
        else:
            print("\033[31mInvalid Account Number.\033[0m")

def main():
    while True:
        print("\n==[\033[93m Expense Tracker in Python \033[0m]==")
        print('1. Add income')
        print('2. Add expense')
        print('3. View balance')
        print('4. View transaction')
        print('5. Clear Transaction History')
        print('6. Exit')
        choice = input("\033[96m = Choose an option (1-6):  \033[0m").strip().lower()
        print()
        if choice == '1':
            print("\033[92mADD INCOME \033[0m")
            print("\033[1m[Income Descriptions: Salary, Investment, Bonus, Part-time, etc...] \033[0m")
            while True:
                description = input("Enter Income Description: ").strip()
                if description.isalpha():
                    while True:
                        try:
                            amount = float(input("Enter Income Amount: ₱ "))
                            if amount <= 0:
                                print("\033[31mAmount should not be below zero\033[0m")
                                continue
                            else:
                                add_income(description, amount)
                                cbalance = transactions[0]['amount']
                                break  # Exit the inner loop if input is valid
                        except ValueError:
                            print("\033[31mInvalid input: Please enter a number.\033[0m")
                    break  # Exit the outer loop if both inputs are valid
                else:
                    print("\033[31mInvalid input: Description should be consist of letters.\033[0m")

        elif choice == '2':
            print("\033[92mADD EXPENSE \033[0m")
            print("\033[1m[Expense Category: food, transportation, bills etc...]\033[0m")
            while True:
                description = input("Enter Expense Category: ").strip()
                if description.isalpha():
                    while True:
                        try:
                            amount = float(input("Enter Expense Amount: ₱ "))
                            if amount > cbalance:
                                print("\033[31mThe amount you input exceed the current balance.\033[0m")
                            else:
                                add_expense(description, amount)
                                break  # Exit the inner loop if input is valid
                        except ValueError:
                            print("\033[31mInvalid input: Please enter a number.\033[0m")
                    break  # Exit the outer loop if both inputs are valid
                else:
                    print("\033[31mInvalid input: Description should be consist of letters.\033[0m")
        elif choice == '3':
            view_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            clear_transaction_history()
        elif choice == '6':
            print("\033[1;35mExiting...Thank you for using this app :)\033[0m")
            time.sleep(3)
            break
        else:
            print("\033[31m Invalid choice! Please try again. \033[0m")

if __name__ == "__main__":
    main()

