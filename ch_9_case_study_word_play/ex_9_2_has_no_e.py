def has_no_e(w):
    return not ('e' in w)

def percentage(a, b):
    return a / b * 100    

if __name__ == "__main__":
    fin = open('words.txt')
    ii = 0
    jj = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            jj += 1
            print(word)
        ii += 1
    print(f'{percentage(jj, ii):.2f}% of words in the list have no e')
