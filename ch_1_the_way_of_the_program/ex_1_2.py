import math

def time_to_seconds(seconds=0, minutes=0, hours=0):
    s = seconds;
    m2s = 60*minutes;
    h2s = 3600*hours;
    return s + m2s + h2s

def kilometers_to_miles(distance_in_km):
    return distance_in_km/1.61

def avg_running_stats(distance, minutes, seconds):
    t = time_to_seconds(seconds, minutes)
    s = kilometers_to_miles(distance)

    pace = t/s
    remainder, mod = math.modf(pace / 60)
    remainder *= 60
    speed = 3600 / (pace)

    return mod, remainder, speed


if __name__ == '__main__':
    print(f'In 42 seconds there are: {time_to_seconds(42)} seconds')
    print(f'In 42 minutes and 42 seconds there are: {time_to_seconds(42, 42)} seconds')
    print(f'In 42 hours, 42 minutes and 42 seconds there are: {time_to_seconds(42, 42, 42)} seconds')
    print()
    
    print(f'In 10 kilometers there are: {kilometers_to_miles(10):.2f} miles')
    print(f'In a marathon there are: {kilometers_to_miles(42.195):.2f} miles')
    print()
    
    m, s, v = avg_running_stats(10, 42, 42)
    print(f'''If you run 10km in 42min and 42sec
        your average pace is {m:.0f}\'{s:.0f}\"
        your average speed is {v:.2f} miles per hour''')