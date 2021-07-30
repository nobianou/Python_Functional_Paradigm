import math
from graphics import *
def intro():
    print("This program draws a Circle and Y-intercept based on user inputs")
    print()
def user_input():
    radius = eval(input("Enter radius: "))
    yi = eval(input("Enter y intercept: "))
    return radius,yi
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
    point1.draw(win)
    point1.setFill('red')
    point2 = Point(-1*x,yi)
    point2.draw(win)
    point2.setFill('red')
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
    intro()
    radius,yi = user_input()
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

"""
Enter radius: 5
Enter y intercept: 4
"""
