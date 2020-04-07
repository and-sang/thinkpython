# def main():
#     known = {(0, 0):1}
#     for m in range(6):
#         for n in range(6):
#             # print(ack(m, n))
#             print(ack_memo(m, n))


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

def ack_memo(m, n):
    if (m, n) in known:
        return known[(m, n)]

    if m == 0:
        known[(m, n)] = n+1
        return n+1
    elif m > 0 and n == 0:
        return ack_memo(m-1, 1)
    else:
        return ack_memo(m-1, ack_memo(m, n-1))

    

if __name__ == "__main__": 
    # main()
    known = {(0, 0):1}
    for m in range(6):
        for n in range(6):
            # print(ack(m, n))
            print(ack_memo(m, n))
            print(known)