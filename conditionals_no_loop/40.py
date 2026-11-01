password=str(input("Enter your password = "))

if(not password.strip()==""):
    if(len(password)>=8):
        print("Password is valid")
else:
    print("Password is not valid")