from graphics import *

def user_input(input):
    fahrenheit = eval(input.getText())
    return fahrenheit
def process(fahrenheit):
    celsius = (fahrenheit-32)*(5.0/9.0)
    return celsius
def main():
    win = GraphWin("Fahrenheit Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    win.setBackground('Lavender')
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
    fahrenheit = user_input(input)
    celsius = process(fahrenheit)
    output.setText(round(celsius,2))
    button.setText("Quit")
    win.getMouse()
    win.close()
    
main()
