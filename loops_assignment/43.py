num=int(input("Enter a number = "))

total=0

for i in range(1,num+1):
    total+=(i*i*i)

print("Sum of cubes of the numbers you entered is = ",total)