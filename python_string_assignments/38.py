text=input("Enter your text : ")

words=text.split()
shortest=''

for word in words:
    if len(word)>len(shortest):
        shortest=word

print("print longest word is = ",shortest)