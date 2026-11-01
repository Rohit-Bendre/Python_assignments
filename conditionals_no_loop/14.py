char = input("Enter a character = ")[0]

if(char.isalpha()):
    if(char.islower()==True):
        print("Character is lowercase")
    else:
        print("Character is uppercase")
else:
    print("enter a valid character")