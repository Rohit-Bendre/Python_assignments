marks=int(input("Enter your marks = "))
attendence=int(input("Enter your attendence percentage = "))

if(0<attendence<=100 and 0<marks<=100):
    if(marks>40 and attendence>75):
        print("You are eligible for the exam")
    elif(marks<40):
        print("you are not eligible for the exam, because you dont have enough marks")
    elif(attendence<75):
        print("you are not eligible for the exam because you dont have enough attendence")
else:
    print("Enter valid details")
