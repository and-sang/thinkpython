import time

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_get(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d

def elapsed_time(f):
    def wrapper(*args, **kwargs):
        global i
        t1 = time.time()
        res = f(*args, **kwargs)
        t2 = time.time()
        if i in args:
            print(f'{f.__name__}({i}): {(t2 - t1)*1e3} ms')
        return res
    return wrapper

@elapsed_time
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@elapsed_time
def fibonacci_memoized(n):
    if n in known:
        return known[n]
    res = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    known[n] = res
    return res

if __name__ == "__main__":
    # print(histogram('hello'))
    # print(histogram_get('hello'))

    known = {0:0, 1:1}
    for i in range(42):
        # t1 = time.time()
        fibonacci(i)
        # t2 = time.time()
        # print(f'FIBONACCI({i}) - Elasped time: {(t2 - t1)*1e3} ms')

        # t3 = time.time()
        fibonacci_memoized(i)
        # t4 = time.time()
        # print(f'FIBONACCI_MEMOIZED({i}) - Elasped time: {(t4 - t3)*1e3} ms')