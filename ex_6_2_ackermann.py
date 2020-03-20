
def ack(m, n):
    # guardian
    if not (isinstance(m, int) or isinstance(n, int)):
        print(f'm, n shall be integers')
        return None
    if m < 0 or n < 0:
        print(f'm, n shall be positive integers')
        return None    

    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))


if __name__ == "__main__":
    print(ack(3, 4))
    print(ack(30, 40))
    print(ack(3, 4))