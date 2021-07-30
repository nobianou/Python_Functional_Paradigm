def squareEach(nums):
    squared_list = []
    for num in nums:
        squared_list.append(num**2)
    return squared_list

def sumList(squared_list):
    sum = 0
    for i in range(len(squared_list)):
                   sum = sum + squared_list[i]
    return sum

def main():
    print("This program   ")  # Add your own description
    numbers = input("Please enter the file name that contains the numbers: ")
    infile = open(numbers,'r')
    nums = []
    for line in infile:
        nums.append(line)
    print(nums)     
    squared_list = squareEach(nums)
    print(squared_list)     
    sum = sumList(squared_list)
    print("The sum of the squares is: ",squared_list)

main()
    
    
    
     

    
