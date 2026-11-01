name=input("Enter name of the customer = ")
bill=int(input("Enter food bill amount = "))
membership=input("Are you a member (Yes/No) = ").lower()
discount=0
service_charge=0
message=''
if(name.strip()!='' and bill>0 and membership in ['yes','no']):
    if(1000<=bill<=2999):
        discount=(bill/100)*5
    elif(3000<=bill<=4999):
        discount=(bill/100)*10
    elif(bill>=5000):
        discount=(bill/100)*15
        message='Thank you for being a valued customer! '
    if(membership=='yes'):
        discount=discount + ((bill/100)*5)
    service_charge=((bill-discount)/100)*5
    final_amount=bill+service_charge-discount
    print("Name of the customer = ",name)
    print("Original bill = ",bill)
    print("Total discount = ",discount)
    print("Service charge = ",service_charge)
    print("Final payable amount = ",final_amount)
    print(message)

else:
    if(name.strip()==''):
        print("Enter valid name!")
    if(bill<=0):
        print("Enter valid bill amount! ")
    if(membership not in ['yes','no']):
        print("Enter valid membership!")

    
