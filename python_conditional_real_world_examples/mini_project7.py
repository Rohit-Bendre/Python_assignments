name=input("Enter name of the customer = ")
plan_type=input("Enter the type of plan (Basic, Standard, Premium) = ").lower()
extra_data=float(input("Extra data used in GB = "))
base_plan_cost=0
extra_data_cost=0
surcharge=0
final_cost=0
if(name.strip()!="" and plan_type in ['basic','standard','premium'] and extra_data>=0):
    if(plan_type=="basic"):
        base_plan_cost=299
    elif(plan_type=="standard"):
        base_plan_cost=499
    elif(plan_type=="premium"):
        base_plan_cost=799

    if(extra_data<=10):
        extra_data_cost=extra_data*20
    elif(extra_data>10):
        extra_data_cost=10*20
        surcharge=100
    final_cost=base_plan_cost+extra_data_cost+surcharge
    print("Name of the customer= ",name)
    print("Base plan type= ",plan_type)
    print("Base plan charge= ",base_plan_cost)
    print("Extra data charge= ",extra_data_cost)
    print("Surcharge= ",surcharge)
    print("Final bill= ",final_cost)


else:
    if(extra_data<0):
        print("Invalid input! You entered negative extra data. ")
    
    print("Please enter valid inputs! ")

