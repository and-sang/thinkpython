from ex_10_10_in_bisect import in_bisect

def reverse_word(w):
    '''return the word reversed
    '''
    return w[::-1]

def wordlist_to_tuple(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

def find_reverse_pairs(wordlist):
    '''return a tuple with all reverse pairs found in wordlist
    '''
    li = list(wordlist)
    revpairs = []
    while li:
        w = li.pop()
        rw = reverse_word(w)
        if in_bisect(li, rw):
            li.remove(rw)
            revpairs.append((w, rw))
            print((w, rw))
    return tuple(revpairs)

if __name__ == "__main__":
    fin = open('words.txt')
    wordlist = wordlist_to_tuple(fin)
    pairs = find_reverse_pairs(wordlist)
    print(f'{len(pairs)} reverse pairs found')