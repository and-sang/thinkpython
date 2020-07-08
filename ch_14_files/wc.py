def main():
    print(linecount('./ch_14_files/wc.py'))

def linecount(filename):
    count = 0
    fin = open(filename, encoding='UTF8')
    for line in fin:
        count += 1
    return count

if __name__ == "__main__": main()