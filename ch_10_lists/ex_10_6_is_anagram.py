def is_anagram(w, x):
    '''takes two words and returns True if they are anagrams
    '''
    if len(w) != len(x):
        return False
    
    wli = list(w)
    xli = list(x)
    while wli:
        c = wli.pop()
        if c in xli:
            xli.remove(c)
        else:
            return False
    return True

if __name__ == "__main__":
    print(is_anagram('abcdefg', 'defgabc'))
    print(is_anagram('abcdefg', 'defggbc'))

