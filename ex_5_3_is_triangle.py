def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print('No')
        return 
    else:
        print('Yes')
        return 1

def user_triangle():
    print(f'let\'s try make a triangle out of three segments')
    a = input('Gimme a segment\n')
    a = int(a)
    b = input('Gimme another one\n')
    b = int(b)
    c = input('Gimme the last one\n')
    c = int(c)

    if is_triangle(a, b, c):
        print(f'you can make a triangle out of those three segments')
    else:
        print(f'you cannot make a triangle out of those three segments')
    return


if __name__ == "__main__":
    # # test no triangle
    # is_triangle(2, 4, 8)
    # is_triangle(4, 8, 2)
    # is_triangle(8, 2, 4)

    # # test degenerate triangle
    # is_triangle(2, 4, 6)
    # is_triangle(4, 6, 2)
    # is_triangle(6, 2, 4)
    
    # test user input
    user_triangle()
    pass