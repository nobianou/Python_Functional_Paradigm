# NOBI ALAM NOUFEEL CSI 31
def  intro():
    print("This program converts a textual message from encripting to decripting and vice-versa based on the shift factor")
    print("The shift factor is known as the key in this program")
    print()
def inputEncript():
    
    message = input("Please enter the message to encode: ")
    key = int(input("Enter the value of the key: "))
    return message,key
def inputDecript():
    msg = input("Please enter the encrypted message for decrypting: ")
    ky = int(input("Enter the key: " ))
    return msg,ky
def processEncript(message,key):
    print("\nThe encripted message is as followed:")
    for ch in message:
        print(ord(ch)+key, end=" ")
    print()
    return
def processDecript(msg,ky):
    chars = [] 
    for char in msg.split():
        codeNum = eval(char)             
        chars.append(chr(codeNum -ky))        

    decrypted_message = "".join(chars)
    
    return decrypted_message

def main():
    intro()
    
    while True:
        enc_or_dec =input("\nPlease enter 1 for Encription or 2 for decription: ")
        enc_or_dec = int(enc_or_dec)
        if enc_or_dec == 1:
            message,key = inputEncript()
            processEncript(message,key)
        elif enc_or_dec == 2:
            msg, ky= inputDecript()
            decrypted_message = processDecript(msg,ky)
            print("\nThe decoded message is:",decrypted_message)
            break
    
main()
"""
This program converts a textual message from encripting to decripting and vice-versa based on the shift factor
The shift factor is known as the key in this program


Please enter 1 for Encription or 2 for decription: 1
Please enter the message to encode: This is crazy.
Enter the value of the key: 3

The encripted message is as followed:
87 107 108 118 35 108 118 35 102 117 100 125 124 49 

Please enter 1 for Encription or 2 for decription: 2
Please enter the encrypted message for decrypting: 87 107 108 118 35 108 118 35 102 117 100 125 124 49
Enter the key: 3

The decoded message is: This is crazy.
"""
