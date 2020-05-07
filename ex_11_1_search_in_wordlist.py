import random
import time

def main():
    fin = open('words.txt')
    d = wordlist_dict(fin)
    fin.close()
    
    fjn = open('words.txt')
    t = wordlist(fjn)
    fjn.close()

    testcase = random_words(t, 10)
    for word in testcase:
        print(word)
        
        t1 = time.time()
        print(in_bisect(t, word))
        t2 = time.time()
        print(f'IN_BISECT - Elasped time: {(t2 - t1)*1e6} ns')
        
        t3 = time.time()
        print(in_dict(d, word))
        t4 = time.time()
        print(f'IN_DICT - Elasped time: {(t3 - t4)*1e6} ns') 
        print()

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f(*args, **kwargs)
        t2 = time.time()
        print(f'{f.__name__} - Elasped time: {(t2 - t1)*1e3} ms')
    return wrapper

def in_bisect(li, el):
    '''implements binary search to find el(ement) in sorted li(st)
    '''
    if not li[:]:   # guard empty list 
        return False

    t = li[:]
    bi = int(len(t)/2)
    if el == t[bi]:
        return True
    elif el < t[bi]:
        # print(f'el: {el}, t[bi]: {t[bi]}\nt[bi:]: {t[:bi]}')
        return in_bisect(t[:bi], el)    # last element of slice not included
    else:
        # print(f'el: {el}, t[bi]: {t[bi]}\nt[bi+1:]: {t[bi+1:]}')
        return in_bisect(t[bi+1:], el)  # first element of slice included, but already checked
    return False

def in_dict(d, key):
    return key in d

def random_words(wordlist, n):
    li = []
    for i in range(n):
        j = random.randint(0, len(wordlist))
        li.append(wordlist[j])
    return tuple(li)

def wordlist_dict(fin):
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = ''
    return d

def wordlist(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

if __name__ == "__main__": main()