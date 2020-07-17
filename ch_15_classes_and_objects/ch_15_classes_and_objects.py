import math
import copy


def main():
    # p1 = Point()
    # print(p1)
    # p1.x = 2
    # p1.y = 2
    # print_point(p1)
    
    # p2 = Point()
    # p2.x = 5
    # p2.y = 6
    # print(distance_between_points(p1, p2))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    
    # center = find_center(box)
    # print_point(center)

    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)

    # print_point(box.corner)
    # move_rectangle(box, 5, 5)
    # print_point(box.corner)

    # a = Point()
    # a.x = 2
    # a.y = 2
    # b = copy.copy(a)
    # print(a is b)
    # print(a == b)   #for instances, == checks object identity, not object equivalence

    # anotherbox = copy.copy(box)
    # print(anotherbox is box)
    # print(anotherbox.corner is box.corner)  # shallow copy

    # print_point(anotherbox.corner)
    # move_rectangle(box, 2, 2)
    # print_point(anotherbox.corner)

    # onelastbox = copy.deepcopy(box)
    # print(onelastbox is box)
    # print(onelastbox.corner is box.corner)  # deep copy

    print_point(box.corner)
    movedbox = move_rectangle_copy(box, 2, 3)
    print_point(box.corner)
    print_point(movedbox.corner)


def move_rectangle_copy(rect, dx, dy):
    '''returns a new Rectangle with corner displaced of dx, dy
    '''
    r = copy.deepcopy(rect)
    r.corner.x += dx
    r.corner.y += dy
    return r

def move_rectangle(rect, dx, dy):
    '''takes a Rectangle and moves its corner of dx, dy
    '''
    rect.corner.x += dx
    rect.corner.y += dy


def grow_rectangle(rect, dwidth, dheight):
    rect.width = rect.width + dwidth
    rect.height = rect.height + dheight

def find_center(rect):
    '''takes a Rectangle as an argument  and returns
    a Point that contains the coordinates of the center
    of the Rectangle
    '''
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def distance_between_points(p1, p2):
    '''takes two Points as arguments and return the distance between them
    '''
    dx = (p2.x - p1.x)**2
    dy = (p2.y - p1.y)**2
    return math.sqrt(dx + dy)


def print_point(p):
    print(f'(x={p.x}, y={p.y})')


class Rectangle():
    '''Represents a rectangle

    attributes: width, height, corner
    '''


class Point:
    '''Represents a point in 2-D space
    '''


if __name__ == "__main__":
    main()