name=input("Enter your name = ")
age=int(input("Enter your age = "))
occupation_risk=input("Enter your occupation risk (Low,Medium,High) = ").lower()
smoker=input("Do you smoke (Yes/No) = ").lower()
eligibility='N/A'
base_premium_cost=10000
high_age_charge=0
occupation_risk_charge=0
smoker_charge=0
additional_charges=0
risk_message="N/a"
if(age>=18 and name.strip()!='' and occupation_risk in ['low','medium','high'] and smoker in ['yes','no']):
    eligibility='Eligible'
    if(age>50):
        high_age_charge=5000
    if(occupation_risk=='high'):
        occupation_risk_charge=7000
    if(occupation_risk=='medium'):
        occupation_risk_charge=3000
    if(smoker=='yes'):
        smoker_charge=5000
    additional_charges=high_age_charge+occupation_risk_charge+smoker_charge
    if(additional_charges>10000):
        risk_message="High risk policy!"
    print("Customer name = ",name)
    print("Eligibilty = ",eligibility)
    print("Base Premium = ",base_premium_cost)
    print("Additional charges = ",additional_charges)
    print("Final premium = ",base_premium_cost+additional_charges)
    print(risk_message)
else:
    if(name.strip()==""):
        print("Enter valid name. ")
    if(age<=0):
        print("Enter valid age! ")
    elif age<18:
        print("You are below 18, so you are not eligible! ")
    if(occupation_risk not in ['low','medium','high']):
        print("Enter valid occupation risk! ")
    if(smoker not in ['yes','no']):
        print("Enter valid smoker type! ")
    print("Eligibility",eligibility)

