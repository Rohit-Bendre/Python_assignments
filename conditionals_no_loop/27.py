print("Enter your login credentials  !")
username=input("Enter your username - ")
password=input("Enter your password - ")

saved_username="RohitBendre35"
saved_password="Rbendre@3542"

if(password==saved_password and username==saved_username):
    print("You logged in successfully! ")
else:
    print("Password or Username is wrong! try again...")