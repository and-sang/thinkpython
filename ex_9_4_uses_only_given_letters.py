import string

def wordlist_to_tuple(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

def uses_only(word, s):
    '''return True if all characters in word are found in s
    '''
    for char in word:
        if char not in s:
            return False
    return True

if __name__ == "__main__":
    fin = open('words.txt')

    t = wordlist_to_tuple(fin)
    s = 'acefhlo'

    for word in t:
        if uses_only(word, s):
            print(word)