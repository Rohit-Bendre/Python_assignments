
strength=0
constains_upper=False
contains_lower=False
contains_digit=False
contains_special=False
password=''
while True:
    ps=input("Enter your password : ")
    if(len(ps.strip())<8):
        print("Password length must be minimum 8 characters ! ")
    else:
        password=ps
        strength+=1
        break

for char in password:
    if char.isupper() and not constains_upper:
        constains_upper=True
        strength+=1
    if char.islower() and not contains_lower:
        contains_lower=True
        strength+=1
    if char.isdigit() and not contains_digit:
        contains_digit=True
        strength+=1
    if char.lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890 ' and not contains_special:
        contains_special=True
        strength+=1

if(strength<=2):
    print("your password is weak !")

elif(strength>2 and strength<5):
    print("Your password is medium !")
else:
    print("Your password is Strong !")


