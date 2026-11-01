num=int(input("enter a number = "))
largest=0

while num!=0:
    if(num%10>largest):
        largest=num%10

    num=num//10
print(largest)