def chop(li):
    '''takes a list and chops its first and last elements
    '''
    del li[0]
    del li[-1]
    return 

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    print(a)
    print(chop(a))
    print(a)