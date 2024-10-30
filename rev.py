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
    print(f"Expense added: {description} - ₱ {amount}")

def view_balance():
    balance = sum(transaction['amount'] for transaction in transactions)
    print(f"Current balance: ₱ {balance:.2f}")

def view_transactions():
    if len(transactions) == 0:
        print("=[No transaction record.]=")
    else:
        print("==Transaction History==")
        print()
        print("[Date stamp | Time stamp | Description | Type | Amount]")
        for transaction in transactions:
            date = transaction['date'].strftime('%Y-%m-%d - %H:%M:%S')
            description = transaction['description']
            amount = transaction['amount']
            type_ = transaction['type']
            print(f"{date} | {description} | {type_} | ₱ {amount:.2f}")

def clear_transaction_history():
    if len(transactions) == 0:
        print("No transaction to delete.")
    else:
        print("==Transaction History==")
        for transaction in transactions:
            date = transaction['date'].strftime('%Y-%m-%d %H:%M:%S')
            description = transaction['description']
            amount = transaction['amount']
            type_ = transaction['type']
            print(f"{date} | {description} | {type_} | ₱ {amount:.2f}")

        choice = int(input("Enter the account number to delete: "))

        if 0 < choice <= len(transactions):
            del transactions[choice - 1]
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
            print("[Income descriptions: Salary, Investment, Bonus, Part-time, etc...]")
            while True:
                try:
                    description = input('enter income description: ')
                    try:
                        amount = float(input('enter income amount: '))
                    except ValueError:
                        
                except ValueError:
                    print("Invalid input")
                    break
                    
                
                
                
                
                
                
                description = input('enter income description: ')
                if description.isalpha():
                    amount = float(input('enter income amount: '))
                    if amount.isinstance():
                        add_income(description, amount)
                    else:
                        print("Invalid Input")
                        break
                else:
                    print("Invalid Input.")
                    break
                add_income(description, amount)
        elif choice == '2':
            print("Expense Category: food, transportation, bills etc..., ")
            description = input('Enter Expense Category: ')
            amount = float(input('Enter Expense Amount: ₱ '))
            add_expense(description, amount)
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

