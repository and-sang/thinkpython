def is_sorted(li):
    '''returns True if the list is sorted in ascending order
    '''
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True


if __name__ == "__main__":
    a = [1,2,3,4,5]
    b = [1,2,4,3,5]
    c = [1,2,3,5,4]

    print(is_sorted(a))
    print(is_sorted(b))
    print(is_sorted(c))