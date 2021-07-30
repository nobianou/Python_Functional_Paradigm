def user_input():
    file_name = input("Enter file name: ")
    infile = open(file_name, "r")
    return file_name,infile
def process(infile):
    line_count = 0
    word_count = 0
    char_count = 1
    for line in infile:
        words = line.split()
        line_count +=1
        line = line[:-1].replace(' ','')
        char_count = char_count + len(line)
        word_count = word_count + len(words)
    return line_count,char_count,word_count
def main():
    file_name,infile = user_input()
    line_count,char_count,word_count = process(infile)
    print("{0} has {1} line {2} words and {3} characters".format(file_name,line_count,word_count,char_count))
    
main()
"""
Enter file name: mytext.txt
mytext.txt has 2 line 2 words and 7 characters
"""
