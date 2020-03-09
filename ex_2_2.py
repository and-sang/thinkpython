import math
import datetime 
from datetime import timedelta

def volume_sphere(r):
    v = (4 / 3) * math.pi * (r**3)
    return v

def book_order(n_copies, cover_price, percent_discount):
    shp_first = 3    # shipping costs for the first book
    shp_rest = 0.75 # shipping costs for each other book
    
    book_price = cover_price * (1 - percent_discount / 100)
    
    if n_copies != 0:
        shipping = shp_first
        if n_copies > 1:
            shipping += shp_rest * (n_copies - 1)
    else:
        return None

    # print(f'book price: {book_price:.2f} $')
    # print(f'shipping price: {shipping:.2f} $')
    order_price = n_copies * book_price + shipping
    return order_price

def workout_end(workout_start, easy_miles, tempo_miles):
    easy = easy_miles * timedelta(minutes=8, seconds=15)
    tempo = tempo_miles * timedelta(minutes=7, seconds=12)
    t = datetime.datetime.combine(datetime.date.today(), workout_start)
    t += easy + tempo
    return t.time()

if __name__ == '__main__':
    # for i in range(0,100,15):
    #     r = i
    #     v = volume_sphere(r)
    #     print(f'the volume of a sphere of radius {r:.1f} mm is {v:.2f} mm^3')

    # orders = (0, 1, 10, 60)
    # for n in orders:
    #     price = book_order(n, 24.95, 40)
    #     if price:
    #         print(f'the order of {n} copies costs {price:.2f} $\n')
    #     else:
    #         print(f'the order of {n} copies is invalid\n')

    workout_start = datetime.time(hour=6, minute=52)
    easy_miles = 2
    tempo_miles = 3
    breakfast_time = workout_end(workout_start, easy_miles, tempo_miles)
    print(f'starting running at {workout_start}, I\'ll have breakfast at {breakfast_time}')