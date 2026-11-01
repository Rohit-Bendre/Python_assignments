num=int(input("Enter a number = "))
number=num
total=0
while number!=0:
    total=total+(number%10)
    number=number//10
print(total)
