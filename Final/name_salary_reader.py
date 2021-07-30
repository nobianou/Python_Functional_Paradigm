def intro():
    print("This Program reads text file and prints out header line and User name and Salary")
    print()
def getInfile():
    text_file = input("What's the text file name: ")
    return text_file
def readWrite(text_file):
    infile = open(text_file, "r")
    print("LastName      FirstName        Salary")
    print("---------------------------------------")
    
    for line in infile:
        fname,lname,salary = line.split()
     
        print("{}             {}        {}".format(lname,fname,salary))

    return infile    


    

def main():

    intro()
    
    text_file = getInfile()
    infile = readWrite(text_file)
    
    infile.close()
   


main()
