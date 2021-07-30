import math
from graphics import *
def intro():
    print("This program draws a Circle and Y-intercept based on user inputs")
    print()
def rad_check():
    while True:
        try:
            radius = eval(input("Enter radius less than 10: "))
            
        except ValueError:
            print("Sorry, enter something valid")
            continue
        if radius>10 or radius<1:
            continue
        else:
            break
    return radius
def yi_check(radius):
    while True:
        try:    
            yi = eval(input("Enter y intercept in the interval [-{},{}]: ".format(radius,radius)))
        except ValueError:
            print("Sorry, enter something valid")
            continue
        if yi<-radius or yi>radius:
            continue
        else:
            break
    return yi
def process(radius,yi):
    x = math.sqrt(abs((radius*radius)-(yi*yi)))
    return x
def circle(radius,win):
    c = Circle(Point(0,0),radius)
    c.draw(win)
    return
def line(yi,win):
    l = Line(Point(-10,yi),Point(10,yi))
    l.draw(win)
    return
def point(x,yi,win):
    point1 = Point(x,yi)
    circ1 = Circle(point1,0.30)
    circ1.setFill('red')
    circ1.draw(win)

    point2 = Point(-1*x,yi)
    circ2 = Circle(point2,0.30)
    circ2.setFill('red')
    circ2.draw(win)

    return
def text(x,win):
    s = Text(Point(-3,-6),"X values are:")
    s.setSize(10)
    s.draw(win)
    x = round(x,2)
    t1 = Text(Point(2.5,-6),x)
    t1.draw(win)
    tOr = Text(Point(5,-6),"Or,")
    tOr.draw(win)
    t2 = Text(Point(8,-6),-x)
    t2.draw(win)
    return
def main():
    radius = rad_check()
    yi = yi_check(radius)
    win = GraphWin()
    win.setCoords(-10,-10,10,10)
    circle(radius,win)
    line(yi,win)
    x = process(radius,yi)
    point(x,yi,win)
    text(x,win)
    ex = Text(Point(-4,7),"Click to exit")
    ex.setSize(12)
    ex.draw(win)
    win.getMouse()
    win.close()

main()

