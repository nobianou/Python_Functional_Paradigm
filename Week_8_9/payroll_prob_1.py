def main():

    print("This program calculates total wage for one week")
    print()
    employees = int(input("How many employees: "))
    payroll = 0
    for employee in range(employees):
        total_hours = int(input("Enter total number of hours worked: "))
        hourly_rate = int(input("Enter  hourly rate: "))
        if total_hours > 40:
            bonus = (total_hours - 40)*(hourly_rate*1.5)
            pay = (40*hourly_rate)+bonus
        elif total_hours <= 40:
            pay = total_hours*hourly_rate
        payroll = payroll + pay
    print("The total payroll for the week is: ",payroll)
    
    
    
main()

        
