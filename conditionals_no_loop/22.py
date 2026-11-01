work_years=int(input("Enter your years of work - "))
salary=int(input("Enter your salary - "))
if(work_years>=0 and salary>0):
    if(work_years<=2 ):
        bonus=(salary/100)*5
        print("your bonus is - ",bonus)
    elif(work_years>2 and  work_years<=5):
        bonus=(salary/100)*10
        print("your bonus is - ",bonus)
    elif(work_years>5 and work_years<=15):
        bonus=(salary/100)*15
        print("your bonus is - ",bonus)
    else:
        bonus=(salary/100)*20
        print("your bonus is - ",bonus)
else:
    print("Enter valid inputs! ")
