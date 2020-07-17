import math
import copy

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
    hole = Circle()
    hole.center = Point()
    hole.center.x = 150
    hole.center.y = 100
    hole.radius = 75

    deg45 = math.sqrt(2)/2

    # pointInside = Point()
    # pointInside.x = hole.center.x + 0.8 * deg45 * hole.radius
    # pointInside.y = hole.center.y + 0.8 * deg45 * hole.radius
    # print(point_in_circle(pointInside, hole))

    # pointOnBoundary = Point()
    # pointOnBoundary.x = hole.center.x + deg45 * hole.radius
    # pointOnBoundary.y = hole.center.y + deg45 * hole.radius    
    # print(point_in_circle(pointOnBoundary, hole))
    
    # pointOutside = Point()
    # pointOutside.x = hole.center.x + 1.2 * deg45 * hole.radius
    # pointOutside.y = hole.center.y + 1.2 * deg45 * hole.radius
    # print(point_in_circle(pointOutside, hole))


    # rectInside = Rectangle()
    # rectInside.corner = copy.copy(hole.center)
    # rectInside.width = 0.8 * deg45 * hole.radius
    # rectInside.height = 0.8 * deg45 * hole.radius
    # print('rectInside: ', rect_in_circle(hole, rectInside))

    # rectOnBoundary = Rectangle()
    # rectOnBoundary.corner = copy.copy(hole.center)
    # rectOnBoundary.width = 1 * deg45 * hole.radius
    # rectOnBoundary.height = 1 * deg45 * hole.radius
    # print('rectOnBoundary: ', rect_in_circle(hole, rectOnBoundary))

    # rectOutside = Rectangle()
    # rectOutside.corner = copy.copy(hole.center)
    # rectOutside.width = 1.2 * deg45 * hole.radius
    # rectOutside.height = 1.2 * deg45 * hole.radius
    # print('rectOutside: ', rect_in_circle(hole, rectOutside))


    cornerInside = Rectangle()
    cornerInside.corner = copy.copy(hole.center)
    # move the corner 0.8*deg45 from the center of the circle
    cornerInside.corner.x += 0.8 * deg45 * hole.radius
    cornerInside.corner.y += 0.8 * deg45 * hole.radius
    cornerInside.width = 200
    cornerInside.height = 200
    print('cornerInside: ', rect_circle_overlap(hole, cornerInside))

    cornerOnBoundary = copy.deepcopy(cornerInside)
    # put back the corner at the center of the circle, then move it 1x away
    cornerOnBoundary.corner.x += (1/0.8)
    cornerOnBoundary.corner.y += (1/0.8)

    print('cornerOnBoundary: ', rect_circle_overlap(hole, cornerOnBoundary))

    cornerOustide = copy.deepcopy(cornerInside)
    # put back the corner at the center of the circle, then move it 1.2x away    
    cornerOustide.corner.x = (1.2/0.8)
    cornerOustide.corner.y = (1.2/0.8)
    print('cornerOustide: ', rect_circle_overlap(hole, cornerOustide))    


def rect_circle_overlap(c, r):
    '''takes a Circle and a Rectangle objects
    returns True if any of the corners of the rectangle 
    falls inside the circle
    '''
    cornersInCircle = []
    for point in rect_corners(r):
        cornersInCircle.append(point_in_circle(point, c))

    return True in cornersInCircle



def rect_corners(r):
    '''takes a Rectangle object
    return its corners as a list of Point objects
    '''
    a = copy.copy(r.corner)
    b = copy.copy(a)
    b.x += r.width
    c = copy.copy(a)
    c.x += r.width
    c.y += r.height
    d = copy.copy(a)
    d.y += r.height
    return [a, b, c, d]


def rect_in_circle(c, r):
    '''takes a Circle and a Rectangle objects
    returns True if the Rectangle lies entirely or on the boundary of the circle
    '''
    for point in rect_corners(r):
        if not point_in_circle(point, c):
            return False
    return True


def point_in_circle(p, c):
    '''takes a Point and a Circle objects
    returns True if Point lies within the Circle, False otherwise
    '''
    return distance_between_points(p, c.center) <= c.radius


def distance_between_points(p1, p2):
    '''takes two Points as arguments and return the distance between them
    '''
    dx = (p2.x - p1.x)**2
    dy = (p2.y - p1.y)**2
    return math.sqrt(dx + dy)





if __name__ == "__main__":
    main()