# NOBI ALAM NOUFEEL     CSI 31

def intro():
    print("This program generates Syracuse sequence for any natural number.")
def user_input():
    number = int(input("Enter the natural number for generating the sequence: "))
    return number
def process(number):
    print(number, end = " , ")
    while number>1:
        if number % 2 == 0:
            number = int(number/2)
            print(number, end = " , ")
        elif number%2 != 0:
            number = int(3*number + 1)
            print(number, end = " , ")

def main():
    intro()
    number = user_input()
    process(number)
main()

"""
This program generates Syracuse sequence for any natural number.
Enter the natural number for generating the sequence: 18
18 , 9 , 28 , 14 , 7 , 22 , 11 , 34 , 17 , 52 , 26 , 13 , 40 , 20 , 10 , 5 , 16 , 8 , 4 , 2 , 1 ,
"""
       
