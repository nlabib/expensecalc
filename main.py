import csv

totalBalance = 0.00
useexit = False


# Show balance by calculating from file
def balance():
    total = 0.00
    try:
        with open('expenses.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                total += float(row[1])  # row[1] = amount
        print("💰 Your balance is $", round(total, 2))
    except FileNotFoundError:
        print("📁 No expenses found yet. Start by adding income or expense.")


# Add an expense
def addExpense():
    extype = "expense"
    amount = float(input("Enter expense: "))
    description = input("Enter description: ")
    with open('expenses.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([description, -amount, extype])
    print(f"✅ Added expense of ${amount:.2f} for {description}")


# Add an income
def addIncome():
    extype = "income"
    amount = float(input("Enter income: "))
    description = input("Enter description: ")
    with open('expenses.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([description, amount, extype])
    print(f"✅ Added income of ${amount:.2f} for {description}")


# Menu loop
while not useexit:
    print("\n===== Expense Tracker Menu =====")
    print("1. Check Balance")
    print("2. Add Expense")
    print("3. Add Income")
    print("4. Exit")

    userinput = input("Enter your choice: ")
    if userinput == "1":
        balance()
    elif userinput == "2":
        addExpense()
    elif userinput == "3":
        addIncome()
    elif userinput == "4":
        useexit = True
        print("👋 Exiting. Goodbye!")
    else:
        print("❌ Invalid choice. Try 1-4.")
