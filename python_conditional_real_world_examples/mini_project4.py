name=input("Enter your name: ")
percentage=float(input("Enter your percentage: "))
family_income=float(input("Enter your family annula income: "))
attendance=float(input("Enter your attendance percentage: "))
eligibility_status=""
scrl_category=""
reason_for_ineligibility=""
if(percentage>=75 and family_income<=400000 and attendance>=75):
    
    eligibility_status="eligible"
    if(percentage>=90):
        scrl_category="Full Scholarship"
        print("Congratulations ",name,"! You are eligible for full scholarship.")
    else:
        scrl_category="Partial Scholarship"
        print("Congratulations ",name,"! You are eligible for partial scholarship.")
else:
    eligibility_status="not eligible"
    if(percentage<75):
        reason_for_ineligibility+="Percentage is less than 75%. "
    if(family_income>400000):
        reason_for_ineligibility+="Family income is more than 400000.  "
    if(attendance<75):
        reason_for_ineligibility+="Attendance is less than 75%. "
    print("Sorry ",name,"! You are not eligible for scholarship.")

print("Student name: ",name)
print("Eligibility status: ",eligibility_status)
print("Scholarship category: ",scrl_category if scrl_category else "N/A")
print("Reason for ineligibility: ",reason_for_ineligibility if reason_for_ineligibility else "N/A")
