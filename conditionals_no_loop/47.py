role=int(input("Enter your role = "))

match role:
    case 1:
        print("You are an Admin")
    case 2:
        print("You are a User")
    case 3:
        print("You are a Guest")
    case _:
        print("Please enter a valid role number between 1 to 3")
