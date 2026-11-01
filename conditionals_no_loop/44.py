traffic=int(input("Enter the traffic in = "))

match traffic:
    case 1:
        print("Traffic is low")
    case 2:
        print("Traffic is medium")
    case 3:
        print("Traffic is high")
    case _:
        print("Please enter a valid number between 1 to 3")