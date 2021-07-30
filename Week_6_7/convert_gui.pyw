from graphics import *

def main():
    win = GraphWin("Fahrenheit Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    Text(Point(1,3), "   Fahrenheit Temperature:").draw(win)
    Text(Point(1,1), "Celsius Temperature:").draw(win)
    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1),"")
    output.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    win.getMouse()
    fahrenheit = eval(input.getText())
    celsius = (fahrenheit-32)*(5.0/9.0)
    output.setText(celsius)
    button.setText("Quit")
    win.getMouse()
    win.close()
    
main()
