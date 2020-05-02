def main():
    w = generate_wordlist('words.txt')
    d = map_anagrams(w)
    
    # l = sorted(d.values(), key=len, reverse=True)
    # for anagrams in l:
    #     if len(anagrams) > 4:
    #         print(anagrams)

    print(most_possible_bingos(d))
        

def map_anagrams(wordlist):
    ''' return a dict which keys are tuples of letters sorted in alphabetical order, 
    and which values are words in wordlist that are composed of those letters
    '''
    l = list(wordlist)
    d = dict()
    result = dict()
    while l:
        word = l.pop()
        t = tuple(sorted(word))
        if d.get(t):
            result[t] = result.setdefault(t, d.get(t)) + [word]
        else:
            d[t] = [word]
    return result

def most_possible_bingos(anagrams_dict):
    ''' return the collection of 8 letters that forms the highest number of anagrams
    '''
    l = sorted(anagrams_dict.values(), key=len, reverse=True)
    for anagrams in l:
        if len(anagrams[0]) == 8:
            return tuple(sorted(anagrams[0])), anagrams

def generate_wordlist(path):
    fin = open(path)
    l = []
    for line in fin:
        l.append(line.strip())
    return tuple(l)



if __name__ == "__main__": main()