text=input("Enter your text : ")

words=text.split()
longest=''

for word in words:
    if len(word)>len(longest):
        longest=word

print("print longest word is = ",longest)