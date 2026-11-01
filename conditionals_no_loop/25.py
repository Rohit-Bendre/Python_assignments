side1=int(input("Enter first side of triangle = "))
side2=int(input("Enter second side of triangle = "))
side3=int(input("Enter third side of triangle = "))

if(side1>=0 or side2>=0 or side3>=0):
    if(side1 != side2 !=side3):
        print("Triangle is scalene")
    elif(side1==side2==side3):
        print("Triangle is equilateral")
    else:
        print("Triangle is isosceles")
else:
    print("Enter valid sides of triangle")
