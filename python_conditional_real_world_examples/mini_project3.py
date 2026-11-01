Name=input("Enter your name: ")
curr_balance=float(input("Enter your current balance: "))
witdhdraw_amount=float(input("Enter the amount to withdraw: "))

if(0<witdhdraw_amount<=curr_balance):
 
    curr_balance=curr_balance-witdhdraw_amount
    print("Account holder name: ",Name)
    print("Transaction status: Successful")
    print("Amount withdrawn: ",witdhdraw_amount)
    print("Current balance: ",curr_balance)


    if(curr_balance<=1000):
        print("Your balance is low. ")
else:
    print("Invalid input. Please enter amount between 0 and your current balance \nbut less than 20000 at a time to withdraw.")
    print("Transaction status: Failed")
    print("Current balance: ",curr_balance)

