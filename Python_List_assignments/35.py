lst1=[1,6,2,35,23,90,21,67,68,23,12,2]

largest=lst1[0]
sec_largest=largest

for digit in lst1:
    if digit>largest:
        sec_largest=largest
        largest=digit

if(sec_largest==largest):
    print("there is no second largest number in the list ")
else:
    print("the second largest number is ",sec_largest)
