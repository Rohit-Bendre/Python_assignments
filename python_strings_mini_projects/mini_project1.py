'''text analyzer'''
text=input("Enter your text : ")
words=text.split()
vowels=0
consonants=0
digits=0
special_chars=0
word_exist=False
for char in text:
    if char in 'aeiou':
        vowels+=1
    if char not in 'aeiou':
        consonants+=1
    if char.lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890 ':
        special_chars+=1
    if char.isdigit():
        digits+=1

search_word="hello"
if search_word in words:
    word_exist=True

word_freq={}
for word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1

cleaned_txt=" ".join(text.split())
print("Total number of characters = ",len(text))
print("Number of vowels = ",vowels)
print("Number of consonants = ",consonants)
print("Number of digits = ",digits)
print("Number of special characters = ",special_chars)
print("Text in lowercase = ",text.lower())
print("Text in uppercase = ",text.upper())
print(f"Is the word {search_word} exist in your text : ")
print("Frequency of words: ")
print(word_freq)
print("Cleaned Text : ",cleaned_txt)

