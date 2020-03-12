import turtle
import math
import random



def polygon(t, sidelength, n):
    startat = random.randint(0, 360)
    vertexangle = 360/n
    for i in range(n):
        t.seth(startat + i*vertexangle)
        triangle(t, sidelength, vertexangle)
    return

def triangle(t, base, vertexangle):
    leg = (base / 2) / math.sin(math.radians(vertexangle) / 2)
    baseangle = (180 - vertexangle) / 2

    t.rt(vertexangle / 2)
    move_and_turn(t, leg, (180 - baseangle))
    move_and_turn(t, base, (180 - baseangle))
    move_and_turn(t, leg, (180 - (vertexangle / 2)))
    

def move_and_turn(t, length, angle):
    t.fd(length)
    t.lt(angle)
    return    

if __name__ == '__main__':
    bob = turtle.Turtle()
    
    # for base in range(100, 200, 20):
    #     triangle(bob, base, 30)

    # for vertexangle in range(30, 75, 15):
    #     triangle(bob, 200, vertexangle) 

    for n in range(4, 10, 1):
        polygon(bob, 100, n)

    turtle.mainloop()