import time

def format_elapsed_time(elapsed_seconds):
    s = elapsed_seconds % 60
    m = elapsed_seconds // 60
    h = m // 60
    m = m % 60
    d = h // 24
    h = h % 24
    return d, h, m, s


if __name__ == "__main__":
    epoch = time.gmtime(0) #platform dependent
    # print(epoch)
    # print()
    t = time.time()
    d, h, m, s = format_elapsed_time(t)

    print(f'Right now you are living: {time.ctime(t)}')
    print(f'Since {epoch.tm_year}-{epoch.tm_mon}-{epoch.tm_mday}, {t} seconds have passed')
    print(f'that is: {d:.0f} days, {h:.0f} hours, {m:.0f} minutes, and {s:.2f} seconds')
