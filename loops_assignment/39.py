
text="Hello my name is rohit bendre"

count=1
incount=False

for char in text:
    if(char!=' '):
        incount=False
    else:
        incount=True
        count+=1


print(count)


