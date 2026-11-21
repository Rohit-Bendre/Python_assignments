str1=input("Enter a string: ")
vowels=0

for char in str1:
    if char.lower() in 'aeiou':
        vowels+=1

print("Number of vowels:", vowels)