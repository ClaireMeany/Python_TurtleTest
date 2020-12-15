#finds the largets element in a list and returns is
def findMax(myList, length):
    
    #base case
    if (length == 1):
        return myList[0]
    return max(myList[length-1], findMax(myList, length-1))
    

#Driver code for findMax
str1=input("Enter numbers seperated by spaces: ")
list1=str1.split(' ')
length = len(list1)
maxNum = findMax(list1, length)
print("The largest number in ", list1, " is ", maxNum)