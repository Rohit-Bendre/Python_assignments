str1=input("Enter a string: ")
digitlst=[]

for elem in str1:
    if(elem.isdigit()):
        digitlst.append(int(elem))

print(digitlst)