def main():
    mylist = [1,2,3,4]
    square_list = []
    for num in mylist:
        square_list.append(num**2)
    sum = 0
    for i in range(len(mylist)):
        sum = sum + mylist[i]
    print("the sum is : ",sum)
    print("The squared list is ", square_list)
main()
