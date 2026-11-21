total_emps=int(input("Enter number of employees: "))
employees=[]
net_payroll=0
for i in range (total_emps):
    name=input("Enter name of employee: ")
    base_salary=int(input("Enter base salary of employee: "))
    overtime_hours=int(input("Enter your overtime working hours : "))
    overtime_pay=overtime_hours*200
    gross_salary=base_salary+overtime_pay
    if gross_salary>50000:
        deduction=(gross_salary/100)*10
    else:
        deduction=(gross_salary/100)*5
    net_salary=gross_salary-deduction
    net_payroll+=net_salary
    employees.append([name,base_salary,overtime_hours,overtime_pay,gross_salary,deduction,net_salary])

for employee in employees:
    print(f"Name: {employee[0]} \nGross Salary: {employee[4]} \n Deduction: {employee[5]} \nNet salary: {employee[6]}")
    print("-"*50)
print(f"Total Net Payroll: {net_payroll}")
print("Employee count: ",total_emps)