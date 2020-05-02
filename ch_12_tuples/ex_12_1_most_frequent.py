import re

def most_frequent(string):
    ''' print the letters of string in decreased order of frequency
    '''
    d = char_frequency(string)
    t = sorted(d, key=d.get, reverse=True)
    for char in t:
        print(f'{char} : {d[char]}')
    
    
def char_frequency(string):
    ''' return a dict with single alphabetic characters as keys, and their frequency in string as values
    '''
    res = dict()
    for char in string:
        if char.isalpha():
            res[char] = res.setdefault(char, 0) + 1
    return res

def main():
    print(char_frequency('banana').items())
    print(char_frequency('ban123 *+#ana'))

    most_frequent('banana')
    print()

    fin = open('words.txt')
    l = []
    for line in fin:
        l.append(line.strip())
    s = ''.join(l)
    most_frequent(s)


if __name__ == "__main__": main()
    