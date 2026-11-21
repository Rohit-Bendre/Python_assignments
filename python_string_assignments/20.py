str1=input("Enter a string: ")
char='e'

for i in str1:
    if(i==char):
        str1=str1.replace(i,"")

print(str1)