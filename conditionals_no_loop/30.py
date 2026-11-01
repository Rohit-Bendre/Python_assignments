num=int(input("Enter a number = "))

if(-9<=num<=9):
    print("its a single digit number")
elif(-99<=num<=-10 or 99>=num>=10):
    print("its a double digit number")
elif(-999<=num<=100 or 999>=num>=100):
    print("its a three digit number")
else:
    print("its more than a three digit number ")