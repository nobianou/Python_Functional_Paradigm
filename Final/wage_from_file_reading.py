# NOBI ALAM NOUFEEL     CSI 31

def main():
    print("Program to create a file of usernames and their weekly pay and total payroll in batch mode.")
    print()

    
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")
   
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    payroll = 0
    
    for line in infile:
        print(line)
        # get the first and last names from line
        #last_name, first_name, hourly_rate, total_hours = line.split()
        my_list = line.split()
        my_list[2] = float(my_list[2])
        my_list[3] = int(my_list[3])
        
   
        if my_list[3]> 40:
            bonus = (my_list[3] - 40)*(my_list[2]*1.5)
            pay = (40*my_list[2])+bonus
            
        elif my_list[3] <= 40:
            pay = my_list[3]*my_list[2]

        pay = round(pay,2)
        payroll = payroll + pay
        
        oline = my_list[0]+ ' , ' + my_list[1] + ' $' + str(pay)
        print(oline, file=outfile)

    last_line = "\nThe total payroll for the week is: " + "$"+ str(round(payroll,2))

    print(last_line, file = outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()
