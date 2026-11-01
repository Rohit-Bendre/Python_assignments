age= int(input("Enter traveller's age = "))
if (age>0 and age<150):
    if(age<5):
        print("Traveller's age is under 5 years, so the ticket cost is free")
    elif(age>5 and age<12):
        print("Traveller is a grown child, so ticket price is half")
    elif(age>12 and age<60):
        print("Traveller is an adult, so the ticket price is full")
    else:
        print("Traveller is a senior citizen, so the ticket price is half")
else:
    print("Enter valid age")
