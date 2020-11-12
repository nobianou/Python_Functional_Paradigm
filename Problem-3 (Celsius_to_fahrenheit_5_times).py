#CSI 31 / D02   NOBI ALAM NOUFEEL Problem-3 (Celsius_to_fahrenheit_5_times).py
# A program that will convert celsius to fahrenheit from 5 executed input
def main():
    print("This program computes celsius to fahrenheit five times.")
    for celsius in range(5):
        celsius =eval( input("Enter the temperature to be converted: "))
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print ("The temperature is equivalent to", round(fahrenheit), "degrees Fahrenheit.")
main()
"""
This program computes celsius to fahrenheit five times.
Enter the temperature to be converted: 10
The temperature is equivalent to 50 degrees Fahrenheit.
Enter the temperature to be converted: 0
The temperature is equivalent to 32 degrees Fahrenheit.
Enter the temperature to be converted: 20
The temperature is equivalent to 68 degrees Fahrenheit.
Enter the temperature to be converted: 30
The temperature is equivalent to 86 degrees Fahrenheit.
Enter the temperature to be converted: 40
The temperature is equivalent to 104 degrees Fahrenheit.
"""
