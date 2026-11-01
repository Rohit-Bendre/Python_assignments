string=input("Enter string = ").lower()
count=0
for i in string:
    if(i in ['a','i','e','o','u']):
        count+=1

print("Total vowels in string = ",count)