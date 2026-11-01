grade=str(input("Enter your grade = "))

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Please enter a valid grade (A, B, or C)")