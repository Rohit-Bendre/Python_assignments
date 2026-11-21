sample_PIN=3459


attempts=3
attempts_used=0
access_status="Denied"
while attempts:
    User_PIN=int(input("Enter your PIN: "))
    attempts_used+=1
    if User_PIN==sample_PIN:
        print("-"*50)
        print("Acsess granted")
        access_status="Granted"
        break
    else:
        attempts-=1
        print(f"Incorrect PIN!)")
        print(f"You have {attempts} attempts left.")


print("-"*50)
print(f"Attempts used: {attempts_used}")
print(f"Access status: {access_status}")
if attempts==0:
    print("You have used all your attempts. ")
    print(f"Your card is blocked temporaritliy.")