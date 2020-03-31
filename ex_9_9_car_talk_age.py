for i in range(10, 40, 1):    # already unreasonable age difference
    counter = 0
    for j in range(99 - i):
        d = str(j).zfill(2)
        m = str(j+i).zfill(2)
        if d == m[::-1]:
            print(f'daughter: {d}, mother: {m}')
            counter += 1
    print(f'{counter} occasions with age difference: {i} years') 