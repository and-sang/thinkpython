def is_power(a, b):
    ''' a is a power of b if: 
         - a divisible by b
         - a/b is a power of b
    '''
    # guardian
    if not (isinstance(a, int) and isinstance(b, int)):
        print('a, b must be integers')
        return None
    if (a*b == 0 or a < b):
        print('a, b must be non-zero integers, a must be bigger than b')
        return None

    if a % b:
        return False
    elif a == b:
        return True
    else:
        return is_power(a//b, b)

    


    pass


if __name__ == "__main__":
    # # test guardian
    # print(is_power('100', 10))
    # print(is_power(100, 10.0))
    # print(is_power(0, 10))
    # print(is_power(10, 100))

    print(is_power(100, 10))
    print(is_power(101, 10))
    print(is_power(125, 5))
    print(is_power(49, 7))