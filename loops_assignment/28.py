num=input("Enter a number = ")
digits=len(num)
number =int(num)
total=0
while number != 0:
    total=total+((number%10)**digits)
    number=number//10

if int(num)==total:
    print("Its a armstrong number .")
else:
    print("Its not a armstrong number .")