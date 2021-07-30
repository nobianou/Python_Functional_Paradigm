def intro():
    print("This program calculates square root of a number using Newton's method.")
    print()
    return
def userInput():
    x = int(input("Enter a positive integer for computing square root: "))
    t = int(input("How many times to perform Newton's method: "))
    print()
    return x,t
def process(x,t):
    guess = x/2
    for i in range(t):
        guess = (guess + (x/guess)) / 2
    diff =abs( x - guess**2)
    return guess,diff
def main():
    intro()
    x,t = userInput()
    guess,diff = process(x,t)
    print("The square root of",x,"is approximately",round(guess,2))
    print("The difference between",x,"and the square of ",guess,"is",round(diff,2))
main()
"""
This program calculates square root of a number using Newton's method.

Enter a positive integer for computing square root: 625
How many times to perform Newton's method: 6

The square root of 625 is approximately 25.0
The difference between 625 and the square of  25.001746971327186 is 0.09
"""
