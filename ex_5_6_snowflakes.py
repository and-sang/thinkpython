import turtle
import math
import random

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def koch(t, l):
    x = l/3
    angle = 60
    if x < 3:
        t.fd(x)
        t.lt(angle)
        t.fd(x)
        t.rt(2*angle)
        t.fd(x)
        t.lt(angle)
        t.fd(x)
    else:
        koch(t, x)
        t.lt(angle)
        koch(t, x)
        t.rt(2*angle)
        koch(t, x)
        t.lt(angle)
        koch(t, x)

def snowflake(t, l, n):
    startat = random.randint(0, 360)
    vertexangle = 360/n
    for i in range(n):
        t.seth(startat - i*vertexangle)
        koch(t, l)
    return

if __name__ == "__main__":
    bob = turtle.Turtle()
    # draw(bob, 5, 5)
    # koch(bob, 90)
    snowflake(bob, 90, 6)
    turtle.mainloop()