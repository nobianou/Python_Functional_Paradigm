from math import *
def intro():
    print("This program calculates the area of a triangle from the length of three arms")
    return
def user_input():
    a = int(input("Enter the length of 1st arm: "))
    b = int(input("Enter the length of 2nd arm: "))
    c = int(input("Enter the length of 3rd arm: "))
    return a,b,c
def process(a,b,c):
    s = (a + b + c) / 2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area
def main():
    intro()
    a,b,c = user_input()
    if (a+b>c and a+c>b and b+c>a):
        area = process(a,b,c)
    else:
        print("The line segement will not form a triangle")
        print("Please give a different input")
        return
    print("The area of a triangle is: ",round(area,2))
main()
"""
This program calculates the area of a triangle from the length of three arms
Enter the length of 1st arm: 2
Enter the length of 2nd arm: 3
Enter the length of 3rd arm: 4
The area of a triangle is:  2.9
"""
"""
This program calculates the area of a triangle from the length of three arms
Enter the length of 1st arm: 1
Enter the length of 2nd arm: 2
Enter the length of 3rd arm: 3
The line segement will not form a triangle
Please give a different input
"""
