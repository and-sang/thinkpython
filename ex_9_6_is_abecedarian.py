import string

def wordlist_to_tuple(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

def is_abecedarian(word):
    '''return True if all characters in word are found in s
    '''
    i = 0
    for char in word:
        if ord(char) < i:
            return False
        else:
            i = ord(char)
    return True

if __name__ == "__main__":
    fin = open('words.txt')

    t = wordlist_to_tuple(fin)

    for word in t:
        if is_abecedarian(word):
            print(word)