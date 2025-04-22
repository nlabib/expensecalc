import csv
totalBalance = 0.00
useexit = False

with open('expenses.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)


#Main balance
def balance():
    global totalBalance
    with open('expenses.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            totalBalance += float(row[1])
    print("Your balance is $", totalBalance)

def addExpense():
    global totalBalance
    expense = float(input("Enter expense: "))
    totalBalance -= expense
    with open('expenses.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([input("Enter description: "), expense])

def addIncome():
    global totalBalance
    income = float(input("Enter income: "))
    totalBalance += income
    with open('expenses.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([input("Enter description: "), income])

while not useexit:
    print("1.Balance")
    print("2.Add Expense")
    print("3.Add Incone")
    print("4.Exit")
    userinput = input("Enter your choice: ")
    userinput = int(userinput)
    if (userinput == 1):
        balance()
    elif (userinput == 2):
        addExpense()
    elif (userinput == 3):
        addIncome()
    elif (userinput == 4):
        useexit = True


