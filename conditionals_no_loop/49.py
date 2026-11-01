result=int(input("Enter your result = "))

match result:
    case 1:
        print("you are passed")
    case 2:
        print("you are failed")
    case 3:
        print("you are absent")
    case 4:
        print("your result is pending")
    case _:
        print("Please enter a valid result number between 1 to 4")