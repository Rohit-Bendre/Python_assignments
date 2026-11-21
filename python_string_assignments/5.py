str1=input("Enter a string: ")
consonants=0

for char in str1:
    if char.lower() not in 'aeiou':
        consonants+=1

print("Number of consonants:", consonants)