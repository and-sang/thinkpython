
class Time:
    '''represents the time of the day

    attributes: hour, minute,second
    '''


def main():
    time = Time()
    time.hour = 1
    time.minute = 0
    time.second = 0
    
    a = mul_time(time, 3)
    print(a.hour, a.minute, a.second)

    time.minute = 20
    b = mul_time(time, 3)
    print(b.hour, b.minute, b.second)

    c = mul_time(time, 1/4)
    print(c.hour, c.minute, c.second)

    my1stMarathon = Time()
    my1stMarathon.hour = 12
    my1stMarathon.minute = 42
    my1stMarathon.second = 3

    my1stMarathon_pace = race_pace(my1stMarathon, 42)
    print(my1stMarathon_pace.hour, my1stMarathon_pace.minute, my1stMarathon_pace.second)    # more likely a netflix marathon


def race_pace(racetime, distance):
    avg_pace = mul_time(racetime, 1/distance)
    return avg_pace


def mul_time(time, multiplier):
    res = multiplier * time_to_int(time)
    return int_to_time(res)


def int_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t


def time_to_int(time):
    minutes = 60*time.hour + time.minute
    seconds = 60*minutes + time.second
    return seconds


if __name__ == "__main__":
    main()