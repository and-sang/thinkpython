import time

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        f(*args, **kwargs)
        t2 = time.time()
        print(f'Elasped time: {(t2 - t1)*1e3} ms')
    return wrapper

@elapsed_time
def listappend(fin):
    print('Function: listappend')
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

@elapsed_time
def listcat(fin):
    print('Function: listcat')
    res = []
    for line in fin:
        word = line.strip()
        res += word
    return res

if __name__ == "__main__":
    fin = open('words.txt')
    listappend(fin)
    fin = open('words.txt')
    listcat(fin)