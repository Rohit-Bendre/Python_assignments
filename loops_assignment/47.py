num=int(input("Enter anumber = "))
product=1

while(num!=0):
    product*=(num%10)
    num=num//10

print("Product of digits of the number you entered = ",product)