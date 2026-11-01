num=input("Enter a number = ")
smallest=int(num[0])

for digit in num:
    if(int(digit)<smallest):
        smallest=int(digit)

print("Smallest number is = ",smallest)