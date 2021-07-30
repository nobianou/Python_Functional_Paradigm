#CSI 31     NOBI ALAM NOUFEEL   quadratics.py
# This program calculates the vertex and y-intercept of a parabola
def main():
    print("This program will calculate the vertex and y-intercept of a parabola from quadratic equation")
    print()
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    c = int(input("Enter the value for c: "))
    x = -b/(2*a)
    y = a*x**2 + b*x + c
    y_int = c
    print("The vertex of the parabola as an ordered pair ({},{}) and the y-intercept is (0,{}). ".format(int(x),int(y),int(y_int)))
main()
