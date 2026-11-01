name=input("Enter your name = ")
age=int(input("Enter your age = "))
show_type=input("Enter show type (Morning or Evening) = ").lower()
day_type=input("Enter day type (Weekday or Weekend) = ").lower()
base_ticket_price=200
discount=0
surcharge=0
final_ticket_price=0
if(name.strip()!="" and age>0 and show_type in ['morning','evening'] and day_type in ['weekday','weekend']):
    if(age<12):
        discount=(base_ticket_price/100)*50
    elif(age>=60):
        discount=(base_ticket_price/100)*30

    if(show_type=='morning'):
        discount+=30

    if(day_type=='weekend'):
        surcharge=50
    print("Customer name = ",name)
    print("Original ticket price = ",base_ticket_price)
    print("Discount = ",discount)
    if(surcharge):
        print("Weekend surcharge = ",surcharge )
    final_ticket_price=base_ticket_price+surcharge-discount
    print("Final ticket price = ",final_ticket_price)

else:
    print('Please enter valid data.')
    if(name==""):
        print("Name cannot be empty.")
    if(show_type not in ['morning','evening']):
        print("Enter valid show type.")
    if(day_type not in ['weekday','weekend']):
        print("Enter valid day type.")
    if(age<=0):
        print("Age must be greater than zero, and cannot be negative.")


