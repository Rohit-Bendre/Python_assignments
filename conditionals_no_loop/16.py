num1, num2,num3=input("Enter three numbers = ").split()

if(num1>num2):
    if(num1>num3):
        print(num1," Is greater ")
    else:
        print(num3, " Is greater")
else:
    if(num2>num3):
        print(num2," Is greater")
    else:
        print(num3," Is greater")