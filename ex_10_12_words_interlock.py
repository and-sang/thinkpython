from ex_10_10_in_bisect import in_bisect

def unlock(word):
    w = word[0::2]
    x = word[1::2]
    return w, x

def unlock_3(word):
    w = word[0::3]
    x = word[1::3]
    y = word[2::3]
    return w, x, y

def wordlist(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return li

if __name__ == "__main__":

    # print(unlock('ababab'))
    # print(unlock('abababa'))
    # print(sorted(('aa', 'bbb', 'c', 'dddd', 'ee'), key=len, reverse=True))

    fin = open('words.txt')
    alphasorted = wordlist(fin)
    lensorted = sorted(alphasorted, key=len, reverse=False)
    interlocked = []
 
    # while len(lensorted[-1]) >= 2*len(lensorted[0]):
    #     word = lensorted.pop()
    #     w, x = unlock(word)
    #     alphasorted.remove(word)
    #     if in_bisect(alphasorted, w) and in_bisect(alphasorted, x):
    #         interlocked.append((word, w, x))
    #         print(interlocked[-1])

    while len(lensorted[-1]) >= 3*len(lensorted[0]):
        word = lensorted.pop()
        w, x, y = unlock_3(word)
        alphasorted.remove(word)
        if in_bisect(alphasorted, w) and in_bisect(alphasorted, x) and in_bisect(alphasorted, y):
            interlocked.append((word, w, x, y))
            print(interlocked[-1])