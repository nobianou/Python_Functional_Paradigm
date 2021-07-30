def main():
    print("This program calculates total wage for one week")
    total_hours = int(input("Enter total number of hours worked: "))
    hourly_rate = int(input("Enter  hourly rate: "))
    if total_hours > 40:
        bonus = (total_hours - 40)*(hourly_rate*1.5)
        wage_total = (40*hourly_rate)+bonus
        print("The total wage including bonus is: ",wage_total)
    elif total_hours <= 40:
        wage_total = total_hours*hourly_rate
        print("The total wage is: ", wage_total)
main()
        
    
