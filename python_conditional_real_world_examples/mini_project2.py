name=input("Enter your name: ")
amount=int(input("Enter purchase amount : "))
customer_type=int(input("1.regular 2.premium \nEnter customer type :"))
discount=0
delivery_charges=0
if(name.strip()=="" or amount<0 or customer_type not in [1,2]):
    print("Please enter valid details!")
else:
    if(amount>=5000):
        discount=(amount/100)*20
    elif(3000<=amount<=5000):
        discount=(amount/100)*10
    elif(1000<=amount<=3000):
        discount=(amount/100)*5

    if(customer_type==2 and discount!=0):
        discount= discount + ((amount/100)*5)
    if(amount<2000):
        delivery_charges=100
    
    payable=amount-discount+delivery_charges
    print("Customer name : ",name)
    print("Total discount : ",discount)
    print("Delivery charges : ",delivery_charges)
    print("Final payable amount : ",payable)