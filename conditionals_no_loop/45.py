menu_order=int(input("Enter your menu order = "))

match menu_order:
    case 1:
        print("You have ordered Pizza")
    case 2:
        print("You have ordered Burger")
    case 3:
        print("You have ordered Pasta")
    case 4:
        print("You have ordered Sandwich")
    case 5:
        print("You have ordered French Fries")
    case _:
        print("Please enter a valid menu order")