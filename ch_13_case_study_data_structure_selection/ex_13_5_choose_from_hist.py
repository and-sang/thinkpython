import random
from collections import Counter

def main():
    h1 = {'a': 2, 'b': 1}
    results = choose_from_hist(h1, 10000)
    print(Counter(results))

def choose_from_hist(hist, nchoices):    
    '''take a histogram and return a random value from it, chosen with
    probability in proportion to frequency
    '''
    t = sorted(hist, key=hist.get, reverse=True)
    w = sorted(hist.values(), reverse=True)
    return random.choices(t, weights=w, k=nchoices)


if __name__ == "__main__":
    main()