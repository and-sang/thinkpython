import re
import string
import random

def main():
    book = 'A Tale of Two Cities'

    textfile = r'ch_13_case_study_data_structure_selection\The Project Gutenberg EBook of ' + book + '.txt'
    print(f'*** BOOK ANALYSIS: {book}\n')
    book_histogram = book_analysis(textfile)
    print(pick_random_word(book_histogram))
    print()


def pick_random_word(histogram):
    ordered_keys = sorted(histogram, key=histogram.get)
    cumfreq = [1]
    for word in ordered_keys:
            cumfreq.append(cumfreq[-1] + histogram.get(word))
    random_pick = random.randrange(1, 1 + cumfreq[-1])
    pick_idx = bisearch(cumfreq, random_pick)
    ## NOTICE: bisearch finds pick_idx so that cumfreq[n] < pick_idx < cumfreq[n+1]
    ## but the values between cumfreq[n] and cumfreq[n+1] are instances of the word in ordered_keys[n+1]
    pick_idx = 1 + pick_idx
    print(ordered_keys[pick_idx])
    return ordered_keys[pick_idx]

def bisearch(ordered_list, value, idx=0):
    size = len(ordered_list)
    divide = int(size / 2)
    if size == 1:
        return idx
    elif ordered_list[divide] < value:
        return bisearch(ordered_list[divide:], value, idx+divide)
    elif ordered_list[divide] > value: 
        return bisearch(ordered_list[:divide], value, idx)
    else:
        return idx + divide

def book_analysis(textfile):    
    wordlist = read_wordlist()
    book = read_book(textfile)
    words = words_analysis(book)
    return words


def words_analysis(book):
    histogram = dict()
    for word in book:
        histogram[word] = 1 + histogram.setdefault(word, 0)
    return histogram
     

def most_frequent(d, x):
    result = []
    t = sorted(d, key=d.get, reverse=True)
    for word in t[:x-1]:
        result.append((word, d[word]))
    return result     


def read_book(textfile):
    # read the book
    fin = open(textfile, encoding='utf-8')    
    book = []

    isHeader = True
    to_clean = re.compile('\W')

    for line in fin:
        # skip over the header information
        if isHeader:
            isHeader = header(line)
        # skip over the footer information
        elif footer(line):
            return tuple(book)
        else:
            book = book + read_line(line, to_clean)

def header(line):
    end_of_header = 'START OF'
    return end_of_header not in line

def footer(line):
    start_of_footer = 'END OF'
    return start_of_footer in line

def read_line(line, to_clean):
    cleanedLine = []
    words = to_clean.split(line)
    for word in words:
        if word.isalpha():
            cleanedLine.append(word.lower())    
    return cleanedLine

def read_wordlist():
    fin = open('words.txt')
    wordlist = dict()
    for line in fin:
        word = line.strip()
        wordlist.setdefault(word, None)
    return wordlist

if __name__ == "__main__":
    main()