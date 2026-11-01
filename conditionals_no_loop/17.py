marks=int(input("Enter your marks = "))

if(marks<=100 and marks>=80):
    print("You passed with A grade")
elif(marks<=79 and marks>=60):
    print("you passed with B grade")
elif(marks<=59 and marks>40):
    print("you passed with C grade")
elif(marks<=39 and marks>0):
    print("You failed the exam")
else:
    print("Enter valid marks")