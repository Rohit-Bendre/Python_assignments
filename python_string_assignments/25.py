str1=input("Enter a string: ")
alphlist=[]

for elem in str1:
    if(elem.isalpha()):
        alphlist.append(elem)

print(alphlist)