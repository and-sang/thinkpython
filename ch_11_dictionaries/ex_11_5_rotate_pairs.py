def main():
    # open wordlist file, return it as a dict
    d = wordlist()

    # check for rotate pairs in wordlist, return them as a dict
    pairs = rotate_pairs(d)

    # print result
    for key in sorted(pairs):
        print(key)

def rotate_pairs(wordlist):
    d = dict()
    for key in wordlist:
        if key[::-1] in wordlist:
            d[(key, key[::-1])] = ''
    return d

def wordlist():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        d[word] = ''
    return d

if __name__ == "__main__": main()