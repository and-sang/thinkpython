def has_duplicates(li):
    '''returns True if there are duplicate elements in the list
    '''
    t = li[:]
    while t:
        el = t.pop()
        if el in t:
            return True
    return False

if __name__ == "__main__":
    print(has_duplicates([1,2,3,4,5,6,7,8]))
    print(has_duplicates([1,2,3,4,5,5,7,8]))
    print(has_duplicates([[1,2,3,4],[5,6,7,8]]))
    print(has_duplicates([[1,2,3,4],[1,2,3,4]]))         