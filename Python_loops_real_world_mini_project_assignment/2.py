print("STUDENTS MARKS SYSTEM ")
students=[]
average_marks=0

num_students=int(input("Enter number of students: "))
pass_count=num_students
fail_count=0
for i in range(num_students):
    name=input(f"Enter name of student {i+1}: ")
    marks=int(input(f"Enter marks of student {i+1}:"))
    while True:
        if marks<0 or marks>100:
            print("Invalid marks! Please enter marks between 0 and 100.")
            marks=int(input(f"Enter marks of student {i+1}:"))
        else:
            break
    average_marks+=marks
    result="pass"
    if marks>=75:
        grade="A"
    elif marks>=60 and marks<75:
        grade="B"
    elif marks>=50 and marks<60:
        grade="C"
    elif marks>=40 and marks<=50:
        grade="D"
    else:
        fail_count+=1
        pass_count-=1
        result="fail"
        grade="none"
    students.append([name,marks,grade,result])
    print("-"*50)

for student in students:
    print(f"Name: {student[0]} \nGrade: {student[2]}")
    print("-"*50)
print(f"Average marks of the class: {average_marks/num_students}")
print(f"Number of students passed: {pass_count}")
print(f"Number of students failed: {fail_count}")