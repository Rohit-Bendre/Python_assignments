import string

text=input("Enter your text : ")

cleaned_txt=text.translate(str.maketrans("","",string.punctuation))

print("Cleaned text = ",cleaned_txt)