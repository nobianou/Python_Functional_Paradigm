#CSI 31 / D02   NOBI ALAM NOUFEEL Problem-2 (average).py
# A program that will calculate the average from  'n' number of inputs
def main():
    print("This program calculates average from n number of inputs")
    sum = 0
    n = int(input("Enter the number of inputs to take: "))
    for i in range(n):
        numb = int(input("Enter the number "))
        sum = sum + numb
    avg = sum/n
    print("The average of those numbers is: ",avg)
main()
"""
This program calculates average from n number of inputs
Enter the number of inputs to take: 3
Enter the number 1
Enter the number 2
Enter the number 3
The average of those numbers is:  2.0
"""
