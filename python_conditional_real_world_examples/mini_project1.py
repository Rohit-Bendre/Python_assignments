name=input("Enter your name: ")
units=int(input("Enter the number of units consumed: "))

bill=0

if(bill>=0):
    if units<=100:
        bill=(units*3)+150

    elif(units>100 and units<=200):
        bill=(100*3)+((units-100)*5)+150

    else:
        bill=(100*3)+(100*5)+((units-200)*7)+150
else:
    print("Invalid input. Please enter a valid number of units.")

print("Name of customer: ",name)
print("Number of units consumed: ",units)
print("Energy charges: ",bill-150)
print("Fixed service charges: 150")
print("Your final electricity bill is: ",bill)
if(bill>=5000):
    print("High Usage bill")