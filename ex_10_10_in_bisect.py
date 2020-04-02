def in_bisect(li, el):
    '''implements binary search to find el(ement) in sorted li(st)
    '''
    if not li[:]:   # guard empty list 
        return False

    t = li[:]
    bi = int(len(t)/2)
    if el == t[bi]:
        return True
    elif el < t[bi]:
        # print(f'el: {el}, t[bi]: {t[bi]}\nt[bi:]: {t[:bi]}')
        return in_bisect(t[:bi], el)    # last element of slice not included
    else:
        # print(f'el: {el}, t[bi]: {t[bi]}\nt[bi+1:]: {t[bi+1:]}')
        return in_bisect(t[bi+1:], el)  # first element of slice included, but already checked
    return False

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10):
        print(in_bisect(a, i))