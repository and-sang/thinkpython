def printall(*args):
    for item in args:
        print(item)
    return

def minmax(t):
    return min(t), max(t)

def sum_all(*args):
    res = 0
    for item in args:
        res += item
    return res

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

if __name__ == "__main__":
    # tuple(sequence)
    t = tuple('banana')
    u = tuple(['b', 'a', 'n', 'a', 'n', 'a'])
    printall(t, u)  # gather multiple arguments in the tuple args

    # tuples are immutable
    print(f't: {t}\nid: {id(t)}')
    t = t + ('s', )
    print(f't: {t}\nid: {id(t)}')

    # tuple assignment
    a = 5
    b = 10
    a, b = b, a
    print(f'a: {a}\nb: {b}')

    print('\nstrictly speaking, a function can only return one value')
    print('but then again, tuple assignment')
    c = (3, 6, 9, 12, 8, 4, 1)
    min_max = minmax(c)
    min_c, max_c = minmax(c)
    print(f'min_max: {min_max}\nmin_c: {min_c}\nmax_c: {max_c}')

    print('Groceries (tuple assignment in traversing a sequence)')
    groceries = [('milk', 2), ('cereals', 1), ('apples', 4)]
    for item, quantity in groceries:
        print(f'{quantity}x {item}')
    
    # scatter
    printall(*t)    # scatter the tuple into multiple arguments (its elements)

    x = (1, -1, 1, -1, 1, -1)
    y = (2, 4, 6, 8)
    print(f'sum_all({x}): {sum_all(*x)}')
    print(f'sum_all({y}): {sum_all(*y)}')

    # zip it!
    s = 'abc'
    li = [0, 1, 2, 3, 4, 5, 6]  # if the sequences are not the same length, the result has the length of the shorter one

    for pair in zip(s, li):
        print(pair)

    print(list(zip(s, li)))

    lj = [8, 9, 10, 11]
    print(list(zip(s, li, lj))) # it works on multiple sequences

    # traversing multiple sequences concurrently
    li01 = [1,2,3,4,5]
    li02 = [6,7,8,9,10]
    li03 = [3,3,3,3,3]
    print(has_match(li01, li02))
    print(has_match(li01, li03))

    # enumerate
    for idx, item in enumerate('banana'):
        print(idx, item)

    d = dict(enumerate('abcde'))
    print(f'd = {d}')


    # dictionaries and tuples
    t = d.items()
    print(t)
    for key, val in t:
        print(key, val)

    # built-in functions
    li = [2,1,3,5,4]
    t = tuple(li)

    li.sort()
    print(li)
    print(sorted(t))

    print(reversed(t))
    for item in reversed(t):
        print(item)
