lst1=[1,6,2,35,23,90,21,67,68,23,12,2]
lst2=[23,12,2,88,77,0,1,35,2,2,35]

lst3=[]
for element in lst1:
    if element in lst2 and element not in lst3:
        lst3.append(element)

print("Common elements = ",lst3)
