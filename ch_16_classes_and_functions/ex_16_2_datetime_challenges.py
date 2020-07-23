from datetime import date, time, datetime, timedelta


def main():
    # which_day_is_today()

    # bday = date(2001, 1, 20)
    # birthday_countdown(bday)

    bday1 = date(1965,5,3)
    bday2 = date(1962,6,24)
    find_n_older_day(bday1, bday2, n=2)
    

def find_n_older_day(birthday1, birthday2, n=2):
    '''takes two birthday date objects and an integer
    return the day
    '''
    lifeExpectancy = 120
    
    if birthday1 > birthday2: 
        return find_n_older_day(birthday2, birthday1, n)

    base1 = birthday1.toordinal()
    base2 = birthday2.toordinal()

    diff = base2 - base1
    death = birthday1.replace(year = birthday1.year + lifeExpectancy)
    lifetime = death.toordinal() - base1

    older = diff
    younger = 0

    for day in range(diff, lifetime):
        older += day
        younger += day
        ageRatio, remainder = divmod(older, younger)
        if ageRatio == n and remainder == 0:
            nday = date.fromordinal(base1 + older)
            print(f'on {nday} user1 is {n}-times older than user 2')
            return 

    print(f'no date was found for which user1 is {n}-times older than user 2')
    

def birthday_countdown(birthday):
    '''takes a datetime object representing a birthday date
    prints the user's age and the time left until the next birthday
    '''
    today = date.today()
    birth = birthday.year + 1
    birthday = birthday.replace(year=today.year)
    
    if birthday < today:
        birthday = birthday.replace(year=today.year+1)
    
    age = birthday.year - birth
    
    birthday = datetime.combine(birthday, time())
    timeleft = birthday - datetime.now()

    print(f'the user is {age} years old')
    print(f'and the time left until the upcoming birthday is')
    print_timeleft(timeleft)

    return timeleft


def print_timeleft(td):
    '''takes a timedelta object (days, seconds)
    prints its value formatted in days, hours, minutes, seconds
    '''
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    print(f'{td.days} days, {h:02d} hours, {m:02d} minutes, {s:02d} seconds')
    return 


def which_day_is_today():
    print(datetime.today().strftime('%A'))


if __name__ == "__main__":
    main()