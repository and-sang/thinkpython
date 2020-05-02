def main():
    wordDict = generate_wordDict('words.txt')
    map_reducible_words(wordDict)
    print(find_longest_reducible_word(wordDict))

def find_longest_reducible_word(wordDict):
    sortedKeys_longestFirst = sorted(wordDict.keys(), key=len, reverse=True)  # start looking from the longest wors in wordDict
    l = sortedKeys_longestFirst[:]
    while l:
        word = l.pop(0)
        if iterate_reducibility(word, wordDict):
            return word
    
def iterate_reducibility(word, wordDict):
    if len(word) < 2:
        return True
    reducibility = wordDict[word]
    if reducibility:  
        for reduced in reducibility:
            return iterate_reducibility(reduced, wordDict)
    else:
        return False
    

def map_reducible_words(wordDict):
    sortedKeys_longestFirst = sorted(wordDict.keys(), key=len, reverse=True)  # start looking from the longest wors in wordDict
    l = sortedKeys_longestFirst[:]
    while l:
        word = l.pop(0)
        for index in range(len(word)):
            temp = list(word)
            temp.pop(index)
            reduced = ''.join(temp)
            if reduced in wordDict:
                wordDict[word].append(reduced)
    return     

def generate_wordDict(path):
    fin = open(path)
    result = dict()
    for line in fin:
        word = line.strip()
        result[word] = list()

    # add single letter words to wordlist
    result['i'] = list()
    result['a'] = list()
    return result

if __name__ == "__main__": main()