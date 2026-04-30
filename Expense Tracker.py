expenses = []

while True:
    print("===================== Welcome to Ali's Expense Tracker =============================")
    print("\n1. Add Expense ")
    print("2. Show Total ")
    print("3. Exit")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        name = input("Enter Expense Name: ")
        amount = float(input("Enter Amount: "))
        expenses.append((name, amount))
        print("✅ Expense Added. ")
    elif choice == "2":
        total = 0 
        print("Your Expenses:\n")
        for name, amount in expenses:
            print(f"{name}: Rs {amount}")
            total += amount
        print(f"\nTotal Spending: {total}")
    elif choice == "3":
        print("Good bye. ")
        break
    else:
        print("Invalid Choice! ")