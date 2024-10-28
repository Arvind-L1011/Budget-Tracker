def show_balance(balance):
    print("*********************")
    print(f"Your balance is ₹{balance}")
    print("*********************")


def add_money():
    print("*********************")
    amount = int(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        return amount


def add_expense(balance):
    print("*********************")
    amount = int(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Budget Tracker    ")
        print("*********************")
        print("1.Show Balance")
        print("2.Add Money")
        print("3.Add Expense")
        print("4.Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += add_money()
        elif choice == '3':
            balance -= add_expense(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")


if __name__ == '__main__':
    main()
