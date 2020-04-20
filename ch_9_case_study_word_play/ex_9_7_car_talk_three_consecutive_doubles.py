import string

def wordlist(fin):
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return tuple(li)

def has_n_consecutive_doubles(word, n):
    if len(word) < 2*n:
        return False

    for i in range(n):
        if word[i*2] != word[i*2+1]:    
            return has_n_consecutive_doubles(word[1:], n)
    return True            




if __name__ == "__main__":
    fin = open('words.txt')
    t = wordlist(fin)

    # print(has_n_consecutive_doubles('aabcde', 1))
    # print(has_n_consecutive_doubles('abbcde', 1))
    # print(has_n_consecutive_doubles('abccde', 1))
    # print(has_n_consecutive_doubles('abcdee', 1))

    # print(has_n_consecutive_doubles('aabccde', 2))
    # print(has_n_consecutive_doubles('aabbcde', 2))
    # print(has_n_consecutive_doubles('abbccde', 2))
    # print(has_n_consecutive_doubles('abcddee', 2))    

    for word in t:
        if has_n_consecutive_doubles(word, 3):
            print(word)