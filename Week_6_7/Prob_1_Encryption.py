# A program to encrypt the message according to its shift factor.
def  intro():
    print("This program converts a textual message into a sequence according to its shift factor")
    print("The shift factor is known as the encription key in this program")
    print()
def userInput():
    message = input("Please enter the message to encode: ")
    key = int(input("Enter the value of the encription key: "))
    return message,key
def solution(message,key):
    print("\nThe encripted message is as followed:")
    for ch in message:
        print(ord(ch)+key, end=" ")
    return
        
def main():
    intro()
    message,key = userInput()
    solution(message,key)
main()
"""
This program converts a textual message into a sequence according to its shift factor
The shift factor is known as key in this program

Please enter the message to encode: Hi there
Enter the value of the key: 3

The encripted message is as followed:
75 108 35 119 107 104 117 104 
"""
