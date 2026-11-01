string=input("Enter a string = ")
reverse_string=""

for i in range(0,len(string)):
    print(string[i])
    reverse_string=string[i]+reverse_string
print("reversed string = ",reverse_string)
