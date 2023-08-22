weekly_budget_input = input("Enter your weekly budget (press enter to skip): ")
weekly_budget = float(weekly_budget_input) if weekly_budget_input else 0

monthly_budget_input = input("Enter your monthly budget (press enter to skip): ")
monthly_budget = float(monthly_budget_input) if monthly_budget_input else 0

if (weekly_budget > 0) or (monthly_budget > 0):
    expenses = []
else:
     print("Invalid input. Please enter a weekly/monthly budget greater than 0.")
     exit()

def add_expense():
    description = input("Enter your expense description: ")
    amount = float(input("Enter your expense amount: "))
    expenses.append({"description": description, "amount": amount})

def show_summary():
    total_expenses = 0
    for expense in expenses:
        total_expenses += float(expense["amount"])

    remaining_budget = (weekly_budget or monthly_budget) - total_expenses

    print("\nExpense Summary: ")
    for expense in expenses:
        print(f"{expense['description']}: £{expense['amount']:.2f}")

    if total_expenses > (weekly_budget or monthly_budget):
        print("Be careful: Expenses exceed your budget!")

while True:
    print("\nExpense Tracker Menu")
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

    choice = input("Select option 1,2 or 3: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid input. Please select a valid option.")

print("Thanks for using the Expense Tracker!")
