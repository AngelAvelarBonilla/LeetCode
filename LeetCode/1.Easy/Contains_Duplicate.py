'''
LeetCode
Difficulty: Easy
217. Contains Duplicates
    Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice 
    in the array, and it should return false if every element is distinct.

My Solution:
    We create an empty set for each run thru the loop we
    check to see if the number is in the Set, if it is not we add it
    If it is than we already know there is a duplicate and we immediately return
    false, If we make it thru the entire array storing every value
    than we know there is no duplicate and we return false
    
Complexity Analysis:

Example:
    We have an array = [1,1]
    An empty set = {}
    First run thru we check to see if 1 is in the set
    it is not so our set is now {1}
    Next we check to see if the next 1 is in the set already.
    It is so we immediately return true
'''
def main():
    input = [1,2,3,1]
    print (containsDuplicates(input))

def containsDuplicates(nums: list) -> bool:
    setOfNums = set()
    for i in range(len(nums)):
        if nums[i] not in setOfNums:
            setOfNums.add(nums[i])
        else:
            return True
            
    return False

main()
