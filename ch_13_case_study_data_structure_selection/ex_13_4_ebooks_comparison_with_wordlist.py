import re
import string

def main():
    a_tale_of = 'A Tale of Two Cities'
    david_cop = 'David Copperfield'
    great_exp = 'Great Expectations'
    hard_time = 'Hard Times'
    oliver_tw = 'Oliver Twist'

    library = (a_tale_of, david_cop, great_exp, hard_time, oliver_tw)

    for book in library:
        textfile = r'ch_13_case_study_data_structure_selection\The Project Gutenberg EBook of ' + book + '.txt'
        print(f'*** BOOK ANALYSIS: {book}\n')
        comparison = book_analysis(textfile)
        print(f'the following {len(comparison)} word have not been found in wordlist')
        for key in comparison:
            print(key)
        print()


    # textfile = r'ch_13_case_study_data_structure_selection\The Project Gutenberg EBook of Hard Times.txt'
    # book_analysis(textfile)
    
def book_analysis(textfile):    

    wordlist = read_wordlist()
    
    book = read_book(textfile)
    words = words_analysis(book)

    return compare_book_with_wordlist(words, wordlist)


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