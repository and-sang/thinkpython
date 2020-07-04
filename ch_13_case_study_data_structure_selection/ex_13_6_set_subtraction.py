import re
import string

def main():
    book = 'A Tale of Two Cities'

    textfile = r'ch_13_case_study_data_structure_selection\The Project Gutenberg EBook of ' + book + '.txt'
    print(f'*** BOOK ANALYSIS: {book}\n')
    dicts_comparison, sets_comparison = book_analysis(textfile)
    print(len(dicts_comparison), len(sets_comparison))
    # textfile = r'ch_13_case_study_data_structure_selection\The Project Gutenberg EBook of Hard Times.txt'
    # book_analysis(textfile)
    
def book_analysis(textfile):    

    wordlist = read_wordlist()
    
    book = read_book(textfile)
    words = words_analysis(book)

    dicts_comparison = compare_book_with_wordlist(words, wordlist)
    sets_comparison = book_analysis_sets(words, wordlist)

    return dicts_comparison, sets_comparison

def book_analysis_sets(words, wordlist):    

    wordlist = set(wordlist)
    words = set(words)

    return words.difference(wordlist)

def compare_book_with_wordlist(book, wordlist):
    not_in_wordlist = dict()
    for key in book:
        if key not in wordlist:
            not_in_wordlist.setdefault(key, None)
    return not_in_wordlist


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