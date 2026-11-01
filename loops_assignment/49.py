while True:
    print("--------MENU-------")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Devision")

    choice=int(input("Enter your choice = "))
    num1=int(input('Enter first number = '))
    num2=int(input('Enter second number = '))
    match choice:
        case 1:
            print("Addition = ",num1+num2)
        case 2:
            print("Substraction =",num2-num2)
        case 4:
            print("Devision = ",num1%num2)
        case 3:
            print("Multiplication = ",num1*num2)
        case _ :
            print("Enter a valid choice")

    continue_=input("Do you want to continue? y/n = ").lower()
    if(continue_=='y'):
        continue_
    else:
        break