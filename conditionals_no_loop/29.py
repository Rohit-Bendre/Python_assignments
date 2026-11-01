print("Enter your details properly : ")
age=int(input("Enter your age - "))
weight=int(input("Enter your weight - "))

if(18<=age<=30 and 45<=weight<=65):
    print("You are eligible for the blood donation")
elif(31<=age<=60 and 60<=weight<=85):
    print("You are eligible for the blood donation")
else:
    print("You are not eligible to donate blood because of your weight or age")