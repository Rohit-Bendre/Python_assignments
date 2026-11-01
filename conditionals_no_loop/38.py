sub1=int(input("Enter marks of subject 1 = "))
sub2=int(input("Enter marks of subject 2 = "))
sub3=int(input("Enter marks of subject 3 = "))

if(sub1>=0 and sub2>=0 and sub3>=0):
    if(sub1>=33 and sub2>=33 and sub3>=33):
        print("You are pass")
    else:
        print("You are fail")
else:
    print("Invalid marks. Please enter marks between 0 and 100.")