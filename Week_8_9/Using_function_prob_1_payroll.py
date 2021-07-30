# NOBI ALAM NOUFEEL     CSI 31
def intro():
    print("This program calculates total wage for one week and the total payroll")
    print()
def user_input():
    employees = int(input("How many employees: "))
    print()
    return employees
def process(employees):
    
    payroll = 0
    for employee in range(employees):
        print()
        total_hours = int(input("{}) Enter total number of hours worked: ".format(employee+1)))
        hourly_rate = int(input("    Enter  hourly rate for employee: ".format(employee+1)))
        if total_hours > 40:
            bonus = (total_hours - 40)*(hourly_rate*1.5)
            pay = (40*hourly_rate)+bonus
            print("    This employees weekly pay is: ",pay)
        elif total_hours <= 40:
            pay = total_hours*hourly_rate
            print("    This employees weekly pay is: ",pay)
            print()

        payroll = payroll + pay
    return payroll
    
def main():

    intro()
    employees = user_input()
    payroll = process(employees)
    
    print("    The total payroll for the week is: ",payroll)
    print()
    
    
    
main()

"""
This program calculates total wage for one week and the total payroll

How many employees: 2


1) Enter total number of hours worked: 50
    Enter  hourly rate for employee: 12
    This employees weekly pay is:  660.0

2) Enter total number of hours worked: 40
    Enter  hourly rate for employee: 12
    This employees weekly pay is:  480

    The total payroll for the week is:  1140.0

"""

        
