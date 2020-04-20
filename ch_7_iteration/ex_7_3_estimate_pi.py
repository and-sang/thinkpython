import math

def estimate_pi(eps = 1e-16):
    k = 0
    pi_inv = 0
    cx = (2 * math.sqrt(2)) / 9801
    
    while True:
        num = math.factorial(k) * (1103 + 26390*k)
        den = (math.factorial(k))**4 * 396**(4*k)
        sumterm = num / den
        pi_inv = pi_inv + cx * sumterm
        pi = 1 / pi_inv
        if sumterm < eps:
            break
        k += 1 
    print(f'k = {k},    sumterm = {sumterm/eps}')
    print(f'estimate_pi:    {pi:.16f}')
    print(f'math.pi:        {math.pi:.16f}')
    print(f'difference:     {abs(pi - math.pi):.16f}')



if __name__ == "__main__":
    for eps in (1e-5, 1e-25, 1e-50, 1e-75, 1e-100, 1e-150):
        estimate_pi(eps)
