yearly_income=int(input("Enter your yearly income = "))
working_years=int(input("Enter your years of income = "))
cibil_score=int(input("Enter your cibil score = "))

if(yearly_income>0 and working_years>0 and cibil_score>0):
    if(yearly_income>100000 and working_years>2 and cibil_score>750):
        print("you are eligible for the loan! ")
    else:
        print("you are not eligible for the loan! ")
else:
    print("Please enter valid details of the questions ")