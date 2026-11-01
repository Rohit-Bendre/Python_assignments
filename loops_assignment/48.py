num=int(input("Enter a number = "))
num_temp=num
total=0

while num_temp!=0:
    factorial=1
    digit=num_temp%10
    for i in range(1,digit+1):
        factorial*=i
    total+=factorial
    num_temp=num_temp//10

if(total==num):
    print("Its a strong number")
else:
    print("Its not a strong number")