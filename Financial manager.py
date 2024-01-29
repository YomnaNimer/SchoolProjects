import datetime

class PersonalFinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, transaction_type, category, description=""):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
            "Date": date,
            "Amount": amount,
            "Type": transaction_type,
            "Category": category,
            "Description": description,
        }
        self.transactions.append(transaction)
        print('Transaction added successfully.')

    def view_transactions(self):
        if not self.transactions:
            print('No transactions found.')
        else:
            print('\n===== Transactions =====')
            for transaction in self.transactions:
                print(f'Date: {transaction["Date"]}, Amount: {transaction["Amount"]}, Type: {transaction["Type"]}, Category: {transaction["Category"]}, Description: {transaction["Description"]}')

    def analyze_finances(self):
        if not self.transactions:
            print('No transactions found.')
        else:
            total_income = sum(transaction["Amount"] for transaction in self.transactions if transaction["Type"] == "Income")
            total_expenses = sum(transaction["Amount"] for transaction in self.transactions if transaction["Type"] == "Expense")
            net_balance = total_income - total_expenses

            print('\n===== Financial Analysis =====')
            print(f'Total Income: {total_income}')
            print(f'Total Expenses: {total_expenses}')
            print(f'Net Balance: {net_balance}')

    def budget_planner(self, budget_amount, category):
        expenses_for_category = [transaction["Amount"] for transaction in self.transactions if transaction["Category"] == category and transaction["Type"] == "Expense"]
        total_expenses_for_category = sum(expenses_for_category)

        print(f'\n===== Budget Planner for {category} =====')
        print(f'Budget Amount: {budget_amount}')
        print(f'Total Expenses: {total_expenses_for_category}')
        remaining_budget = budget_amount - total_expenses_for_category
        print(f'Remaining Budget: {remaining_budget}')

def main():
    finance_manager = PersonalFinanceManager()

    while True:
        print('\n===== Personal Finance Manager Menu =====')
        print('1. Add Transaction')
        print('2. View Transactions')
        print('3. Analyze Finances')
        print('4. Budget Planner')
        print('5. Quit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            amount = float(input('Enter the transaction amount: '))
            transaction_type = input('Enter the transaction type (Income/Expense): ').capitalize()
            category = input('Enter the category: ')
            description = input('Enter a description (optional): ')
            finance_manager.add_transaction(amount, transaction_type, category, description)
        elif choice == '2':
            finance_manager.view_transactions()
        elif choice == '3':
            finance_manager.analyze_finances()
        elif choice == '4':
            budget_amount = float(input('Enter the budget amount: '))
            category = input('Enter the category for budget planning: ')
            finance_manager.budget_planner(budget_amount, category)
        elif choice == '5':
            print('Exiting the Personal Finance Manager application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
