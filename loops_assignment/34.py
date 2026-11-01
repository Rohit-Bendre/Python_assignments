string=input("Enter a string = ")
reversed=""

for i in range(0,len(string)):
    reversed=string[i]+reversed

if(string==reversed):
    print("The string is palindrome")
else:
    print("The string is not palindrome")