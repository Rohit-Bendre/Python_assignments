option=int(input("Enter your option for ATM machine = "))

match option:
    case 1:
        print("You have selected to check balance")
    case 2:
        print("You have selected to withdraw money")
    case 3:
        print("You have selected to deposit money")
    case 4:
        print("You have selected to transfer money")
    case 5:
        print("You have selected to change PIN")
    case _:
        print("Please enter a valid option number between 1 to 5")