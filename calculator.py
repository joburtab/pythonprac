while True:
    print("\nWelcome to take the exam!")
    print("This is an educational question on computer science")

    print("\nMain-Menu")
    print("Addition ---------------- 1")
    print("Subtraction ------------- 2")
    print("Division ---------------- 3")
    print("Multiplication ----------- 4")
    print("Exit --------------------- 5")

    try:
        user = int(input("Select from the given menu: "))
    except ValueError:
        print("Please enter a valid number between 1 and 5.")
        continue

    if user == 1:  # Addition
        no1 = int(input("Please enter how many numbers to be added: "))
        if no1 > 0:
            total = 0
            for i in range(no1):
                no = float(input(f"Enter number {i+1}: "))
                total += no
            print("The sum of the numbers is " + str(total))

    elif user == 2:  # Subtraction
        no1 = int(input("Please enter how many numbers to be subtracted: "))
        if no1 > 0:
            total = float(input("Enter the first number: "))
            for k in range(1, no1):
                number = float(input(f"Enter number {k+1}: "))
                total -= number
            print("The result of the subtraction is " + str(total))

    elif user == 3:  # Division
        count = int(input("Please enter how many numbers to be divided: "))
        if count > 0:
            total = float(input("Enter the first number: "))
            for h in range(1, count):
                no1 = float(input(f"Enter number {h+1}: "))
                if no1 != 0:
                    total /= no1
                else:
                    print("Cannot divide by zero, skipping this number.")
            print("The result of the division is " + str(total))

    elif user == 4:  # Multiplication
        count = int(input("Please enter how many numbers to be multiplied: "))
        total = 1
        for i in range(count):
            no1 = float(input(f"Enter number {i+1}: "))
            total *= no1
        print("The result of the multiplication is " + str(total))

    elif user == 5:
        print("Thanks for using our calculator! Goodbye!")
        break

    else:
        print("Invalid choice. Please choose between 1 and 5.")
