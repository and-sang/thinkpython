class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        res = self.second
        res += 60*self.minute
        res += 3600*self.hour
        return res

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time 


def main():
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 00
    
    Time.print_time(start)
    start.print_time()

    print(start.time_to_int())

    end = start.increment(1337)
    end.print_time()

    print(end.is_after(start))

    noinit = Time()
    noinit.print_time()
    print(noinit)

    duration = Time(1, 35)
    print(start + duration)




if __name__ == "__main__":
    main()