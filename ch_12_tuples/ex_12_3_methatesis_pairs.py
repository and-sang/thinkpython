from ex_12_2_anagrams import map_anagrams



def main():
    wordlist = generate_wordlist('words.txt')
    d = map_anagrams(wordlist)
    pairs = methatesis_pairs(d)
    for pair in pairs:
        print(pair)

def methatesis_pairs(anagramsDict):
    result = list()
    for anagrams in anagramsDict.values():
        temp = anagrams[:]
        while len(temp) > 1:
            word1 = temp.pop()
            for word in temp:
                if is_methatesis_pair(word1, word):
                    result.append((word1, word))
    return tuple(result)

def is_methatesis_pair(word1, word2):
    ''' two words form a methatesis pair if you can transform one into the other by swapping 2 letters
    '''
    counter = 0
    for index in range(len(word1)):
        if word1[index] != word2[index]:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


def generate_wordlist(path):
    fin = open(path)
    l = []
    for line in fin:
        l.append(line.strip())
    return tuple(l)

if __name__ == "__main__": main()