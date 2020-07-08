from ex_12_2_anagrams import generate_wordlist, map_anagrams
import dbm
import pickle


def main():
    wordlist = generate_wordlist('words.txt')
    anagrams = map_anagrams(wordlist)

    dbfile = './ch_14_files/mySecondDB/anagramShelf'
    db = dbm.open(dbfile, 'c')

    store_anagrams(db, anagrams)
    print(read_anagrams(db, 'house'))
    print(read_anagrams(db, 'post'))

    db.close()


def store_anagrams(db, anagrams):
    for key in anagrams:
        dbkey = pickle.dumps(key)
        db[dbkey] = pickle.dumps(anagrams[key])


def read_anagrams(db, word):
    key = tuple(sorted(word))
    
    try:
        values = db[pickle.dumps(key)]
    except:
        print('word not found in the database')
        return

    return pickle.loads(values)



if __name__ == "__main__": main()