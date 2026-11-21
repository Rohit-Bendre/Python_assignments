days=int(input("Enter number of days: "))
total_units=0
average_units=0
days_units_greater_than_10=0
max_units=0

for i in range(days):

    units=int(input(f"Enter units consumed for day {i+1}:"))
    total_units+=units
    if max_units<units:
        max_units=units
    if units>10:
        days_units_greater_than_10+=1

average_units=total_units/days
print(f"Total units consumed: {total_units}")
print(f"Average units consumed per day: {average_units}")
print(f"Days units consumed greater than 10: {days_units_greater_than_10}")
print(f"Maximum units consumed in a day: {max_units}")
if total_units>300:
    print("High Usge Warning! You have exceeded 300 units.")
    