# NOBI ALAM NOUFEEL     CSI 31
import math
from graphics import *
def user_input(win):
    p1 = win.getMouse()
    p2 = win.getMouse()
    return p1,p2

def line_draw(win,p1,p2):
    l = Line(Point(p1.getX(),p1.getY()), Point(p2.getX(),p2.getY()))
    mp = l.getCenter()
    mp.setFill('cyan')
    mp.draw(win)
    l.draw(win)

def slope(win,p1,p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    if dx != 0:
        slope = dy/dx
        s2 = "Slope of the line is: " + str(slope)
        s = Text(Point(220,80),s2)
        s.draw(win)
    elif dx == 0:
        s2 = "The slope cannont be determined"
        s = Text(Point(220,80),s2)
        s.draw(win)
    return dx,dy
def length(win,dx,dy):
    length = math.sqrt(abs((dx*dx) - (dy*dy)))
    s1 = "Length of the line is: " + str(length)
    
    l = Text(Point(220,50),s1)
    l.draw(win)
    

def main():
    win = GraphWin("Line Segment",500,500)
    click = Text(Point(250,15)," This program draws line based on user clicking on")
    click.draw(win)
    
    
    p1, p2 = user_input(win)
    line_draw(win,p1,p2)
    
    dx,dy =slope(win,p1,p2)
    
    length(win,dx,dy)
    
    ex = Text(Point(250,400),"To close the program click anywhere within the window")
    ex.setSize(12)
    ex.draw(win)
    win.getMouse()
    win.close()
main()
    
