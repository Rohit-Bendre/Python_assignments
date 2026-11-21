days=int(input("Enter number of days: "))

total_expense=0
max_expense=total_expense
for i in range(days):
    expense=int(input(f"Enter expense for the day {i+1}: "))
    total_expense +=expense

    if expense>max_expense:
        max_expense=expense

print(f"Total expense so far: {total_expense}")
print(f"maximum epense in one day : {max_expense}")
print(f"Average expense per day: {total_expense/days}")
if total_expense>5000:
    print("Budget Alert! You have exceeded 5000 rs.")

    