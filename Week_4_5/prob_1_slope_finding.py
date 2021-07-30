def intro():
    print("This program calculated the slope of a non-vertical line from two point")
    print()
    return

def userInput():
    x1,y1 = eval(input("Enter the value for (x1,y1): "))
    x2,y2 =eval(input("Enter the value for (x2,y2): "))
    print()
    return x1,y1,x2,y2

def solution(x1,y1,x2,y2):
    m = (y2 - y1)/(x2 - x1)
    return m
    
def main():
    intro()
    x1,y1,x2,y2 = userInput()
    if  (x2-x1) == 0:
        print("Slope cannont be calculated for two point on a vertical line")
        return
    m = solution(x1,y1,x2,y2)
    print("The slope of non vertical line is: ",int(m))

main()
"""
This program calculated the slope of a non-vertical line from two point

Enter the value for (x1,y1): 5,4
Enter the value for (x2,y2): 4,5

The slope of non vertical line is:  -1
"""
"""
This program calculated the slope of a non-vertical line from two point

Enter the value for (x1,y1): 5,6
Enter the value for (x2,y2): 5,8

Slope cannont be calculated for two point on a vertical line
"""
