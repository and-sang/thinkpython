import math

def mysqrt(a):
    x = a/3
    y = x
    eps = 1e-6
    
    while True:
        # print(x)
        y = (x + (a / x)) / 2
        if abs(y - x) < eps:
            break
        x = y
    return y

def test_square_root():
    print('a    mysqrt(a)   math.sqrt(a)    diff')
    print('-    ---------   ------------    ----')
    
    for i in range(1, 10, 1):
        x = mysqrt(i)
        y = math.sqrt(i)
        z = abs(x - y)
        print(f'{i:.1f}  {x:.6f}     {y:.6f}      {z:.6f}')



if __name__ == "__main__":
    # test mysqrt
    # print(mysqrt(2))
    # print()
    # print(mysqrt(4))
    # print()
    # print(mysqrt(9))
    # print()
    # print(mysqrt(625))
    # print()

    test_square_root()