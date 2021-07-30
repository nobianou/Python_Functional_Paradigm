# userfile.py
#    Program to create a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")
   # print(infileName)
    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        print(line)
        # get the first and last names from line
        last_name, first_name, hourly_rate, total_hours = line.split()
        hours_total = int(total_hours[0])
        rate_hourly= int(hourly_rate[0])
        if hours_total > 40:
            bonus = (hours_total- 40)*(hourly_rate*1.5)
            pay = (40*rate_hourly[0])+bonus
            pay = round(pay,2)
            oline = last_name[0] + ',' + first_name[0] + '$  ' + str(pay)
            print(oline, file=outfile)
        elif hours_total<= 40:
            pay = hours_total*rate_hourly
            pay = round(pay,2)
            oline = last_name[0] + ',' + first_name[0] + '$  ' + str(pay)
            print(oline, file=outfile)
        
        #pay = int(hourly_rate[0]) * int(total_hours[0])
        
        
        # write it to the output file
        

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()
