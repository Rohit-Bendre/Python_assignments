lang=int(input("Enter a language number = "))

match lang:
    case 1:
        print("You have selected Python")
    case 2:
        print("You have selected Java")
    case 3:
        print("You have selected C++")
    case 4:
        print("You have selected JavaScript")
    case 5:
        print("You have selected C#")
    case _:
        print("Please enter a valid language number between 1 to 5")