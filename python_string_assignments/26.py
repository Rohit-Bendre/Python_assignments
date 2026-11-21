str1=input("Enter a string: ")
char_to_find='e'

first_occ=str1.find(char_to_find)
sec_occ=str1.rfind(char_to_find)

print("First Occurenece = ",first_occ)
print("Second Occurence = ",sec_occ)
    