
opening_balance = int(input("Enter opening balance: "))
total_transactions = int(input("Enter number of transactions: "))

balance = opening_balance

deposit_count = 0
successful_withdrawals = 0
rejected_withdrawals = 0

for i in range(total_transactions):

    print(f"Transaction {i+1}")

    transaction_type = input("Enter transaction type (D/W): ").upper()
    amount = int(input("Enter transaction amount: "))

    if transaction_type == "D":
        balance += amount
        deposit_count += 1
        print("Deposit successful!")
        print("Current balance:", balance)

    elif transaction_type == "W":
        if amount <= balance:
            balance -= amount
            successful_withdrawals += 1
            print("Withdrawal successful!")
            print("Current balance:", balance)
        else:
            rejected_withdrawals += 1
            print("Insufficient balance! Withdrawal rejected.")
            print("Current balance:", balance)

    else:
        print("Invalid transaction type!")

    print("-" * 50)

print("---------- BANK ACCOUNT SUMMARY ----------")

print("Opening Balance:", opening_balance)
print("Final Balance:", balance)
print("Total Deposits:", deposit_count)
print("Successful Withdrawals:", successful_withdrawals)
print("Rejected Withdrawals:", rejected_withdrawals)

if balance < 1000:
    print("Warning: Your account balance is below ₹1,000.")

print("-" * 50)
