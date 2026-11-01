num=int(input("Enter a number = "))
number=num
rev=0

while(number!=0):
    rev=(rev*10)+(number%10)
    number=number//10
print("Reversed Number= ",rev)