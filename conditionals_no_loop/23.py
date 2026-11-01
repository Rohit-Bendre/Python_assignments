units=int(input("Enter your light units - "))

if(units<50):
    bill=units*7
    print("Your light bill is - ",bill)
elif(units>50 and units<=100):
    bill=(50*7)+((units-50)*11)
    print("Your light bill is - ",bill)
elif(units>100 and units<=200):
    bill=(50*7)+(50*11)+((units-100)*13)
    print("Your light bill is - ",bill)
else:
    bill=(50*7)+(50*11)+(100*13)+((units-200)*17)
    print("Your light bill is - ",bill)