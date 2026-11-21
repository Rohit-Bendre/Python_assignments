lst1=[1,6,2,35,23,90,21,67,68,23,12,2]
lst2=[]
for num in lst1:
    if num%2!=0:
        lst2.append(num)

print("List without even numbers = ",lst2)