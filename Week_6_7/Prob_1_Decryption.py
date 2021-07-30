
# A program to decrypt the encrypted message
def intro():
    print("This program decrypts the encrypted message to its original form based on the key")
    print("The shift factor is known as the key in this program\n")
    print()
def userInput():
    message = input("Please enter the encrypted message for decrypting: ")
    key = int(input("Enter the decription key: " ))
    return message,key
def solution(message,key):
    chars = [] 
    for char in message.split():
        codeNum = eval(char)             
        chars.append(chr(codeNum -key))        

    decrypted_message = "".join(chars)
    
    return decrypted_message

def main():
    intro()
    message, key = userInput()
    decrypted_message = solution(message,key)
    print("\nThe decoded message is:",decrypted_message)
    
    

main()
"""
This program decrypts the encrypted message to its original form based on the key
The shift factor is known as the key in this program


Please enter the encrypted message for decrypting: 75 108 35 119 107 104 117 104
Enter the decription key: 3

The decoded message is: Hi there
"""
