import turtle
import math
import random

def flower(t, chord, r, npetals):
    divangle = math.ceil(360/npetals)
    startat = random.randint(0, 360)
    for i in range(npetals):
        petal(t, chord, r, (startat + i*divangle))


def petal(t, chord, r, axisangle):
    t.seth(axisangle)
    if 2*r < chord:
        print(f'WARNING: the smallest ratio r/chord is 0.5 (full circle)')
        print(f'you chose a ratio of {(r/chord):.1f}, the ratio 0.5 will be used instead')
        r = chord/2
        print(f'the new value assigned to r is {r:.2f}')
    angle = 2 * math.asin(chord / (2 * r))
    angledeg = angle * 180 / math.pi
    t.rt(angledeg / 2)    
    arc(t, r, angle)
    t.seth(axisangle - 180)
    t.rt(angledeg / 2)
    arc(t, r, angle)
    t.seth(axisangle)
    return

def arc(t, r, anglerad):
    arclength = anglerad*r
    polyline(t, r, arclength)
    return

def polyline(t, r, arclength):
    seglength = 0.05 * r # graphical approx polyline to arc as % of arc radius
    circumference = 2 * r * math.pi
    ncircle = math.ceil(circumference / seglength)
    narc = math.ceil((arclength * ncircle) / circumference)
    narc += 1   # consider last segment when range(narc)
    for i in range(narc):
        move_and_turn(t, seglength, 360/ncircle)
    return

def move_and_turn(t, length, angle):
    t.fd(length)
    t.lt(angle)
    return    

if __name__ == '__main__':
    bob = turtle.Turtle()

    # bob.color('red')
    # bob.setpos(-100, 100)
    # for r in range(100, 300, 40):
    #     arc(bob, r, 250)
    #     bob.setpos(-100, 100)
    #     bob.seth(0)

    # bob.color('green')
    # bob.setpos(100, -100)
    # for angle in range(30, 270, 30):
    #     anglerad = angle / 180 * math.pi
    #     arc(bob, 150, anglerad)
    #     bob.setpos(100, -100)
    #     bob.seth(0)

    # bob.color('blue')
    # for axisangle in range(0, 360, 60):
    #     petal(bob, 200, 400, axisangle)

    bob.color('purple')
    flower(bob, 200, 300, 15)

    turtle.mainloop()