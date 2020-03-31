def is_palindrome(s):
    return s == s[::-1]

def odometer_counter(n):
    if n+1 < 1e6:
        n += 1
    else:
        n = 0
    return n, str(n).zfill(6)    

if __name__ == "__main__":
    # print(is_palindrome('aoxomoxoa'))
    # print(str(123).zfill(6))
    # print(type(int('123')))
    # s = str(123456).zfill(6)
    # print(s[-5:])

    for i in range(1000000):
        s = str(i).zfill(6)
        if is_palindrome(s[-4:]) and not is_palindrome(s[-5:]):
            n, t = odometer_counter(i)
            if is_palindrome(t[-5:]) and not is_palindrome(t):
                n, u = odometer_counter(n)
                if is_palindrome(u[1:-1])and not is_palindrome(u):
                    n, v = odometer_counter(n)
                    if is_palindrome(v):
                        print('found it!')
                        print(f'odometer read:\n  {s}\n  {t}\n  {u}\n  {v}\n')