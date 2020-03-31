def print_longer_than(w, n):
    if len(w) >= n:
        print(w)

if __name__ == "__main__":
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        print_longer_than(word, 20)