import string

def avoids(w, s):
    if len(w) < len(s): # use the shortest string for the forbidden chars
        return avoids(s, w)
    for char in s:
        if char in w:
            return False
    return True

def clean_input():
    s = input('Type forbidden letters to sort out the word list\n')
    w = s.strip()
    if not w.isalpha():
        print('Please, don\'t mess around with special characters. Only letters a-z')
        return clean_input()
    return w.lower()

def wordlist_to_tuple(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

def number_of_matches(wordlist, c):
    '''count how many words from wordlist do not have the character c 
    '''
    i = 0
    for word in wordlist:
        if avoids(word, c):
            i += 1
    return i

def avoids_most(wordlist, s):
    '''find the char in s that is found the minimum number of words from wordlist
    '''
    i = 0
    c = ''
    li = []
    for char in s:
        j = number_of_matches(wordlist, char)
        li = []
        if j > i:
            i = j
            c = char
        elif j == i:
            i = j
            li.append((c, i))
    li.append((c, i))
    if len(li) > 1:
        print(li)
        return li
    else:
        return c, i

def filter_wordlist(wordlist, c):
    li = list(wordlist)
    for word in wordlist:
        if not avoids(word, c):
            li.remove(word)
    return tuple(li)


def avoids_combined(wordlist, s, depth):
    '''sort out words from wordlist recursively (number of recursions according to depth)
     - identifies char in s that is found in the minimum number of words from wordlist
     - update s and wordlist to exclude char and the words in which it is present
    '''
    c, i = avoids_most(wordlist, s)
    print(f'sorting out letter {c}, {i} words remaining')
    li = list(s)
    li.remove(c)
    s = ''.join(li)
    wordlist = filter_wordlist(wordlist, c)
    if len(wordlist) != i:
        print(f'new wordlist is {len(wordlist) - i} items different than expected')
    
    if depth > 0:
        depth -= 1
        avoids_combined(wordlist, s, depth)

    return 

if __name__ == "__main__":
    fin = open('words.txt')
    # s = clean_input()
    # for line in fin:
    #     word = line.strip()
    #     if avoids(word, s):
    #         print(word)
    t = wordlist_to_tuple(fin)
    s = string.ascii_lowercase[::-1]
    # for char in s:
    #     print(f'the letter {char} sorts out {len(t) - number_of_matches(t, char)} words from wordlist')
    # print(avoids_most(t, s))
    for depth in range(5):
        print(f'\n\ndepth = {depth}')
        avoids_combined(t, s, depth)