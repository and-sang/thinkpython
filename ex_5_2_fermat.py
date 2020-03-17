def check_fermat(a, b, c, n):
    if not (type(a) is int and type(b) is int and type(c) is int and type(n) is int):
        print(f'INVALID INPUT: inputs shall be integers')
        print(f'a = {a} is {type(a)}')
        print(f'b = {b} is {type(b)}')
        print(f'c = {c} is {type(c)}')
        print(f'n = {n} is {type(n)}')
        return
    if n < 2:
        print(f'INVALID INPUT: n shall be 2 or bigger')
        print(f'n = {n}')
        return 
    eq = a**n + b**n - c**n
    if eq == 0:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work')
    return

def input_fermat():
    print(f'Fermat\'s last theorem says that there are no positive integers a, b, and c such that')
    print(f'    a^n + b^n = c^n')
    print(f'for any values of n greater than 2')
    print()
    print(f'Let\'s prove him wrong')
    print()
    a = input('Gimme an a!\n')
    a = int(a)
    b = input('Gimme a b!\n')
    b = int(b)
    c = input('Gimme a c!\n')
    c = int(c)
    n = input('At last, gimme a n!\n')
    n = int(n)
    return a, b, c, n    

if __name__ == "__main__":
    # # test invalid input
    # check_fermat(1.0, 2, 3, 4)
    # check_fermat(1.0, 2.0, 3.0, 4.0)
    # check_fermat(1,2,3,1)

    # # test invalid Fermat
    # check_fermat(1,2,3,4)
    # check_fermat(4,3,2,2)

    # # test input Fermat
    # a, b, c, n = input_fermat()
    # check_fermat(a, b, c, n)

    # test tuple input
    check_fermat(*input_fermat())