#CSI 31 / D02   NOBI ALAM NOUFEEL Problem-4 (Celsius_to_fahrenheit_0_to_100).py
# A program that will convert celsius to fahrenheit from 0 to 100 degree every 10 interval
def main():
    print(" Celsius \t Fahrenheit")
    print("-------------------------------")
    for celsius in range(0,101,10):
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print("{0:10} {1:10}".format(celsius,round(fahrenheit)))
main()
"""
 Celsius 	 Fahrenheit
-------------------------------
         0         32
        10         50
        20         68
        30         86
        40        104
        50        122
        60        140
        70        158
        80        176
        90        194
       100        212
"""
