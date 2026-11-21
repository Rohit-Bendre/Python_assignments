text=input("Enter your text : ")
word=input("Enter a word to find : ")
words=text.split()

if word in words:
    print("the word exist in the text.")
else:
    print("The word does not exist in the text.")