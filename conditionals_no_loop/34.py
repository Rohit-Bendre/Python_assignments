year=int(input("Enter year = "))

if(year%100==0 and year%400==0) :
	print("Its a centuray and leap year")
else:
	print("Its not a century and leap year")