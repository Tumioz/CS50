words=input("Input: ")
vowels=['a','e','i','o','u']
new_words=""
for letter in words:
    if letter.lower() in vowels:
        new_words=new_words
    else:
        new_words=new_words+letter
print(new_words)