word=input("camel case: ")
new_word=""

for letter in word:
    if letter.isupper():
        new_word=new_word+"_"+letter.lower()
    else:
        new_word=new_word+letter

print(f"snake_case: {new_word}")
        

