def main():
    print("This program generates Syracuse sequence for any natural number.")
    number = int(input("Enter the natural number for generating the sequence: "))
    print(number, end = " , ")

    while number>1:
        if number % 2 == 0:
            number = int(number/2)
            print(number, end = " , ")
        elif number%2 != 0:
            number = int(3*number + 1)
            print(number, end = " , ")
    
main()
        
    
