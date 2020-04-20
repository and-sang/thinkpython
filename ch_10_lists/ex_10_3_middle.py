def middle(li):
    '''takes a list and returns a copy of it without first and last elements
    '''
    return li[1:-1]

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = middle(a)
    print(a, middle(a), b)
