import matplotlib.pyplot as plt

def add_expense(expenses):

    category = input("Enter the category (e.g., Food, Travel): ")
    amount = float(input("Enter the amount (₹): "))
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    print(f"Added ₹{amount:.2f} to {category}.\n")

def view_expenses(expenses):

    if not expenses:
        print("No expenses to display.\n")
        return

    print("\nExpenses:")
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount:.2f}")
    
    labels = expenses.keys()
    sizes = expenses.values()
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct=lambda p: f'₹{p * sum(sizes) / 100:.2f}', startangle=140)
    plt.title("Expense Distribution (₹)")
    plt.show()

def main():

    expenses = {}
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()