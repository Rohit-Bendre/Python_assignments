
table_number = int(input("Enter a positive number for multiplication table: "))

print("------- MULTIPLICATION TABLE ----------")

for i in range(1, 11):
    print(f"{table_number} x {i} = {table_number * i}")

print("--------- NUMBER RANGE ANALYSIS ----------")

start_number = int(input("Enter starting number: "))
end_number = int(input("Enter ending number: "))

even_count = 0
odd_count = 0
total_sum = 0

if start_number > end_number:
    print("Invalid range! Starting number cannot be greater than ending number.")

else:
    for number in range(start_number, end_number + 1):

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        total_sum += number

    print("-------- ANALYSIS RESULT ----------")
    print("Even numbers count:", even_count)
    print("Odd numbers count:", odd_count)
    print("Sum of the range:", total_sum)
