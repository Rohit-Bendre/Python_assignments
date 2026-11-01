bill=int(input("Enter your shopping bill = "))

if(bill>0):
    if(bill<1000):
        print("Sorry your bill is too low, no discount for you...")
    elif(bill>=1000 and bill<5000):
        discount=(bill/100)*5
        final_price=bill-discount
        print("Your discounted bill is = ",final_price)
    elif(bill>=10000 and bill<30000):
        discount=(bill/100)*10
        final_price=bill-discount
        print("Your discounted bill is = ",final_price)
    elif(bill>=20000 and bill<50000):
        discount=(bill/100)*15
        final_price=bill-discount
        print("Your discounted bill is = ",final_price)
    else:
        discount=(bill/100)*12
        final_price=bill-discount
        print("Your discounted bill is = ",final_price)
else:
    print("Enter valid amount! ")