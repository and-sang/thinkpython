import string
import re

def main():
    # read a file
    fin = open('text3.txt')
    cleanWords = list()
    
    regExp_nonalpha = re.compile('\W')

    for line in fin:
        words = regExp_nonalpha.split(line)
        for word in words:
            if word.isalpha():
                cleanWords.append(word.lower())
    cleanText = ' '.join(cleanWords)
    print(cleanText)



if __name__ == "__main__":
    main()