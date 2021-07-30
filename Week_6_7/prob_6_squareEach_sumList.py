def intro():
    print("This program squares each list number and calculates the sum of that squared list numbers.")
    print()
    
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
    intro()
    nums = [1,2,3,4,5,6]
    print("The original list is: " ,nums)
    print()
    squared_list = squareEach(nums)
    print("The squared list is: ", squared_list)
    print()
    sum = sumList(squared_list)
    print("The sum of the squared list is: ",sum)

main()
"""
This program squares each list number and calculates the sum of that squared list numbers.

The original list is:  [1, 2, 3, 4, 5, 6]

The squared list is:  [1, 4, 9, 16, 25, 36]

The sum of the squared list is:  91
"""
    
    
     

    
