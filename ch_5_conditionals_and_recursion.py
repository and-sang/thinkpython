

def min2hour_converter(minutes):
    h = minutes // 60
    m = minutes % 60
    print(f'{minutes} minutes correspond to {h}:{m} ({h} hours and {m} minutes)')
    return h, m

def is_divisible(divisible, by):
    return not (divisible % by) # if zero, then divisible

def exctract_digits(num, lastndigits):
    exp = 10**lastndigits
    return num % exp

def even_or_odd(n):
    if n % 2 == 0:
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
    return

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def airspeed():
    prompt = 'What is the airspeed velocity of an unladen swallow?\n'
    speed = input(prompt)    
    return int(speed)


if __name__ == '__main__':
    # min2hour_converter(45)
    # min2hour_converter(105)
    # min2hour_converter(120)

    # print(is_divisible(100, 5))
    # print(is_divisible(100, 7))
    # print(is_divisible(100, 25))

    # print(exctract_digits(54321, 1))
    # print(exctract_digits(54321, 3))
    # print(exctract_digits(54321, 5))
    # print(exctract_digits(54321, 7))

    # even_or_odd(3)
    # even_or_odd(6)

    # countdown(4)
    # countdown(14)

    # print_n('imparo', 5)

    print(airspeed())