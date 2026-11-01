num1=int(input("Enter first number ="))
num2=int(input("Enter second number ="))

print(" addition- 1 \n substraction -2 \n multiplication -3 \n division -4")
choice=int(input("Enter your choice ="))

match choice:
    case 1:
        print("Addition = ",num1+num2)
    case 2:
        print("Subtraction = ",num1-num2)
    case 3:
        print("Multiplication = ",num1*num2)
    case 4:
        print("Division = ",num1/num2)
    case _:
        print("Please enter a valid choice")