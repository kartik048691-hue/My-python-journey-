#ATM machine

balance = 10000

while True:
    print("          ATM          ")
    print("Type 1 to check balance")
    print("Type 2 for deposit")
    print("Type 3 to withdraw")
    print("Type 4 to exit")

    choice = int(input("Enter your choice: "))

    while choice < 1 or choice > 4:
        print("Invalid option")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is {balance}")

    elif choice == 2:
        amount = int(input("Enter the amount you want to deposit: "))
        balance = balance + amount
        print(f"Your balance is {balance}")

    elif choice == 3:
        amount = int(input("Enter the amount you want to withdraw: "))

        if amount > 0 and amount <= balance and amount % 100 == 0:
            balance = balance - amount
            print(f"Your balance is {balance}")
        else:
            print("Write something valid")

    elif choice == 4:
        print("Thank you for using ATM")
        break