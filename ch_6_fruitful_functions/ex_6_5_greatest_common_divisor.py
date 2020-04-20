def gcd(a, b):
    ''' if r is the remainder when a is divided by b,
    then gcd(a, b) = gcd(b, r)
    '''
    # guardian
    if not (isinstance(a, int) and isinstance(b, int)):
        print('a, b must be integers')
        return None
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(9, 18))
    print(gcd(100, 10))
    print(gcd(13, 7))
    print(gcd(50, 25))

