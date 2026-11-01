total=0
while True:
    num=int(input("Enter a number = "))
    if(num>=0):
        total+=num
    else:
        break

print("Sum of the numbers you entered is = ",total)