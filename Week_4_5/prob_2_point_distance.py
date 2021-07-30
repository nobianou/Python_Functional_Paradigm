def intro():
    print("This program calculates distance between two coordinate points")
    print("It also finds the length of the line segment.")
    print()
def userInput():
    x1,y1 = eval(input("Enter the value for (x1,y1): "))
    x2,y2 = eval(input("Enter the value for (x2,y2): "))
    print()
    return x1,y1,x2,y2
def solution(x1,y1,x2,y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance
def main():
    intro()
    x1,y1,x2,y2 = userInput()
    distance = solution(x1,y1,x2,y2)
    print ("The distance between two points is: ",round(distance,2))
    print()
    print("The length of the line segment is: ",round(distance,2),"units")
main()
"""
This program calculates distance between two coordinate points
It also finds the length of the line segment.

Enter the value for (x1,y1): 4,5
Enter the value for (x2,y2): 5,4

The distance between two points is:  1.41

The length of the line segment is:  1.41 units
"""
