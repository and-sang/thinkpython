def rotate_string(s, n):
    '''take a string and an integer,
    return a string that contains the letters of the original string rotated by the given amount
    '''
    res = []
    for c in s:
        res.append(rotate_char(c, n))
    return ''.join(res)

def rotate_char(c, n):
    '''take a char and an integer,
    return the char rotated by the given amount
    '''        
    a = ord(c)
    uppbase = 65    # uppercase: ord('A')
    lowbase = 97    # lowercase: ord('a')
    nletters = 25   # alphabet length ord('z') - ord('a')

    if uppbase <= a <= uppbase + nletters:
        return chr(uppbase + loop_25(a - uppbase, n))
    elif lowbase <= a <= lowbase + nletters:
        return chr(lowbase + loop_25(a - lowbase, n))
    else:
        return chr(a)

def loop_25(x, n):
    ''' take an integer between 0 and 25 and increases it of the given amount n, 
    return an integer between 0 and 25
    '''
    if n > 25:
        n = n % 25
    
    if x + n > 25:
        return x + n - 26   # length of 0 to 25 is 26
    else:
        return x + n

if __name__ == "__main__":
    
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))

    # print(loop_25(12, 12))
    # print(loop_25(12, 13))
    # print(loop_25(12, 14))
    # print(loop_25(12, 125))

    # print(loop_25(25, 1))
    # print(loop_25(25, 2))

    # print(rotate_char('A', 2))
    # print(rotate_char('Z', 1))
    # print(rotate_char('a', 2))
    # print(rotate_char('z', 2))

    # print(rotate_char('a', 25))
    # print(rotate_char('z', 26))

    print(rotate_string('abcdefg, HIJKLMNOP!', 1))
