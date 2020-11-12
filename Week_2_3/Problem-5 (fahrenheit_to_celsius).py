#CSI 31 / D02   NOBI ALAM NOUFEEL Problem-5 (fahrenheit_to_celsius).py
# A program that converts fahrenheit to celsius.
def main():
    print("A program that converts fahrenheit to celsius.")
    fahrenheit =float( input("Enter the Fahrenheit temperature to be converted: "))
    celsius = (fahrenheit - 32) * .5556
    print ("The temperature is equivalent to", round(celsius), "degrees Fahrenheit.")
main()
"""
A program that converts fahrenheit to celsius.
Enter the Fahrenheit temperature to be converted: 50
The temperature is equivalent to 10 degrees Fahrenheit.
"""
