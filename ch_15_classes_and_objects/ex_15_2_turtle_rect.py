import turtle
import copy
import math


class Circle():
    '''Represents a circle

    attributes: center, radius
    '''


class Rectangle():
    '''Represents a rectangle

    attributes: width, height, corner
    '''


class Point():
    '''Represents a point in 2-D space

    attributes: x, y
    '''


def main():
    bob = turtle.Turtle()

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0    
    draw_rectangle(bob, box)

    anotherBox = copy.deepcopy(box)
    anotherBox.corner.x = 50
    anotherBox.corner.y = 150
    draw_rectangle(bob, anotherBox)

    wheel = Circle()
    wheel.center = Point()
    wheel.center.x = 150
    wheel.center.y = 100
    wheel.radius = 75
    draw_circle(bob, wheel)

    bob.mainloop()


def draw_circle(t, c):
    '''takes a Turtle and a Circle objects
    draws a circle
    '''
    origin = copy.copy(c.center)
    place_turtle(t, c.center)
    
    circumference = 2*math.pi*c.radius
    length = 0.05*c.radius
    n = math.ceil(circumference/length)
    print(f'radius = {c.radius:.2f}\n    length = {length:.2f}\n    n = {n}')
    
    for i in range(n):
        move_and_turn(t, length, 360/n)
    
    bring_turtle_back(t, origin)
    return


def draw_rectangle(t, r):
    '''takes a Turtle and a Rectangle objects
    draws a rectangle with the turtle
    '''
    origin = copy.copy(r.corner)
    place_turtle(t, r.corner)

    for i in range(2):
        move_and_turn(t, r.width, 360/4)
        move_and_turn(t, r.height, 360/4)

    bring_turtle_back(t, origin)
    return


def bring_turtle_back(t, p):
    '''takes a Turtle and a Point object
    the turtle is located at the coordinates given by the point object
    brings back the Turtle at the origin (coordinates (0,0))
    '''
    origin = copy.copy(p)
    origin.x *= -1
    origin.y *= -1
    place_turtle(t, origin)


def place_turtle(t, p):
    '''takes a Turtle (at coordinates (0,0)) and a Point object
    places the Turtle at the Point coordinates
    '''
    t.pu()
    move_and_turn(t, p.x, 90)
    move_and_turn(t, p.y, -90)
    t.pd()


def move_and_turn(t, length, angle):
    t.fd(length)
    t.lt(angle)
    return    


if __name__ == "__main__":
    main()