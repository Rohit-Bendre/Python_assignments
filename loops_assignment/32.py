base=int(input("Enter exponent = "))
exponent=int(input("Enter exponent = "))

i=1
result=1

while (i<=exponent):
    result=result*base
    i+=1

print(result)