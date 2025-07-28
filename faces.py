def convert(emoticon):
    emoticon_emoji={":)":"🙂",":(":"☹️"}
    return emoticon_emoji.get(emoticon)

def main():
    emoji=input("Enter emoticon\n")
    print(convert(emoji))
    
main()
    