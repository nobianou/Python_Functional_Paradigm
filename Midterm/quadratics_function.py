#CSI 31     NOBI ALAM NOUFEEL   quadratics_function.py
# This program calculates the vertex and y-intercept of a parabola
def intro():
    print("This program will calculate the vertex and y-intercept of a parabola from quadratic equation")
    print("The program gets the coefficient(a,b,and c) of a quadratic function")
    return
def userInput():
    a = int(input("Enter the value for coefficient a: "))
    b = int(input("Enter the value for coefficient b: "))
    c = int(input("Enter the value for coefficient c: "))
    return a,b,c
def solution(a,b,c):
    x = -b/(2*a)
    y = a*x**2 + b*x + c
    y_int = c
    return x,y,y_int
def main():
    intro()
    a,b,c = userInput()
    x,y,y_int = solution(a,b,c)
    print("The vertex of the parabola as an ordered pair ({},{}) and the y-intercept is (0,{}). ".format(round(x,2),round(y,2),int(y_int)))
main()
"""
This program will calculate the vertex and y-intercept of a parabola from quadratic equation
The program gets the coefficient(a,b,and c) of a quadratic function
Enter the value for coefficient a: 5
Enter the value for coefficient b: 4
Enter the value for coefficient c: 2
The vertex of the parabola as an ordered pair (-0.4,1.2) and the y-intercept is (0,2).
"""
