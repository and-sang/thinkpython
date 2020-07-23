import copy

class Time:
    '''represents the time of the day

    attributes: hour, minute,second
    '''


def main():
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 5
    print_time(time)

    # t2 = copy.copy(time)
    # print(is_after(time, t2))

    # t2.second = 6
    # print(is_after(time, t2))

    t10 = increment_pure(time, 10)
    t1000 = increment_pure(time, 1000)
    t100000 = increment_pure(time, 100000)

    t10_2 = increment2(time, 10)
    t1000_2 = increment2(time, 1000)
    t100000_2 = increment2(time, 100000)

    time10 = copy.copy(time)
    increment(time10, 10)
    time1000 = copy.copy(time)
    increment(time1000, 1000)
    time100000 = copy.copy(time)
    increment(time100000, 100000)

    print('t10 vs time10 vs t10_2')
    print_time(t10)
    print_time(time10)
    print_time(t10_2)
    print('t1000 vs time1000 vs t1000_2')
    print_time(t1000)
    print_time(time1000)
    print_time(t1000_2)
    print('t100000 vs time100000 vs t100000_2')
    print_time(t100000)
    print_time(time100000)
    print_time(t100000_2)


def increment2(time, seconds):
    total = time_to_int(time) + seconds
    return int_to_time(total)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time    


def increment_pure(time, seconds):
    t = Time()
    m, s = divmod((time.second + seconds), 60)
    h, m = divmod((time.minute + m), 60)
    h += time.hour

    t.second = s
    t.minute = m    
    t.hour = h
    return t

def increment(time, seconds):
    
    m, s = divmod((time.second + seconds), 60)
    time.second = s
    time.minute += m    

    h, m = divmod(time.minute, 60)
    time.minute = m
    time.hour += h


def print_time(t):
    '''takes a Time object
    prints it in the form hour:minute:second
    '''
    print(f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}')

def is_after(t1, t2):
    '''takes two Time objects
    return True if t1 follows t2 chronologically
    '''
    s1 = f'{t1.hour:02d}{t1.minute:02d}{t1.second:02d}'
    s2 = f'{t2.hour:02d}{t2.minute:02d}{t2.second:02d}'
    return s2 > s1




if __name__ == "__main__":
    main()