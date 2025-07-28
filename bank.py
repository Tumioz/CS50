words=input("Greeting: ").lower()
sep_words=words.strip()
nletter=""

for i in range(5):
    letter=sep_words[i]
    nletter=nletter+letter

if nletter=="hello":
    print("$0")
elif nletter[0]=="h":
    print("$20")
else:
    print("$100")


