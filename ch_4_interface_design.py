import turtle
import math

def square(t, length):
    for i in range(4):
        move_and_turn(t, length, 90)
    return

def polygon(t, length, n):
    for i in range(n):
        move_and_turn(t, length, 360/n)
    return

def polyline(t, length, n, ndrawn=None):
    # ndraw - n of segment draw (ndrawn == n in case of a polygon)
    if not ndrawn:
        ndrawn = n
    for i in range(ndrawn):
        move_and_turn(t, length, 360/n)
    return

def circle(t, r):
    circumference = 2*math.pi*r
    length = 0.05*r
    n = math.ceil(circumference/length)
    print(f'radius = {r:.2f}\n    length = {length:.2f}\n    n = {n}')
    polygon(t, length, n)
    return    

def arc(t, r, angle_deg):
    angle = angle_deg * math.pi / 180
    arc_length = angle*r
    circumference = 2*math.pi*r
    length = 0.05*r
    ndrawn = math.ceil(arc_length/length)
    n = math.ceil(circumference/length)
    print(f'radius = {r:.2f}, angle = {angle:.2f}\n    length = {length:.2f}\n    n = {n}\n    ndrawn = {ndrawn}')
    polyline(t, length, n, ndrawn)
    return       

def move_and_turn(t, length, angle):
    t.fd(length)
    t.lt(angle)
    return

if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.color('red')
    for length in range(50,100,5):
        square(bob, length)

    bob.color('green')
    for n in range(3,30,3):
        polygon(bob, 50, n)

    bob.color('blue')    
    for r in range(30,50,4):
        circle(bob, r)

    bob.color('orange')    
    arc_tests = ((30, 90), (40, 180), (50, 270), (60, 360))
    for r, angle in arc_tests:
        arc(bob, r, angle)
        bob.setpos(0, 0)
        bob.seth(0)
    turtle.mainloop()