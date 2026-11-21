text=input("Enter your text : ")

upper=0
lower=0

for char in text:
    if char.isupper():
        upper+=1

    if char.islower():
        lower+=1

print("Total uppercase letters in your text = ",upper)
print("Total lowercase letters in your text = ",lower)