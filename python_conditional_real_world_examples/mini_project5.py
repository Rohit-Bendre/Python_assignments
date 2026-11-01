name=input("Enter your name: ")
salary=int(input("ENter your monthly salary: "))
experience=int(input("Enter your years of experience: "))
performance_rating=int(input("Enter your performance rating (1-5): "))
bonus=0
bonus_percentage=0
message=""
if experience>=0 and salary>0 and name.strip()!="":
    if(1<=performance_rating<=5):
        if(performance_rating==5):
            message="Excellent performer"
        if(experience>=10 and performance_rating>=4):
            bonus=(salary/100)*20
            bonus_percentage=20
        elif(experience>=5 and performance_rating>=4):
            bonus=(salary/100)*15
            bonus_percentage=15
        elif(experience>=2 and performance_rating>=3):
            bonus=(salary/100)*10
            bonus_percentage=10
        print("Employee name: ",name)
        print("Bonus percentage : ",bonus_percentage,"%")
        print("Bonus amount: ",bonus)
        print("final salary: ",salary+bonus)
        print("performance message: ",message if message else "N/A")
    else:
        print("invalid rating, must be between 1 and 5")
else:
    print("Invalid employee details")
