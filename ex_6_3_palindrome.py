def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    # guardian
    if not isinstance(word, str):
        print('input must be a string')
        return False
    
    if len(word) < 2:
        return True
    
    if first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False
    
    

if __name__ == "__main__":
    # # test middle
    # print(middle('abcde'))
    # print(middle('abcd'))
    # print(middle('abc'))
    # print(middle('ab'))
    # print(middle('a'))
    # print(middle(''))

    print(is_palindrome('aoxomoxoa'))
    print(is_palindrome('aoxomo'))
    print(is_palindrome('omo'))
    print(is_palindrome('om'))
    print(is_palindrome('o'))

