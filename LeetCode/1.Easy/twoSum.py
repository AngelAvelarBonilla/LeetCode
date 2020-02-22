'''
LeetCode
Difficulty: Easy
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

My Solution:
- Pass through the list once creating a hash map with the number as the key
and the index as the value.

- Pass through the list again this time checking if the target - the number exists as a key in the hash map

- Return the index of the current number and the value of the key which is also an index

Complexity Analysis:
    Time Complexity: O(n), We pass thru the list containing n elements twice O(2n)
    The hash table's look up time is near constant(Only not being constant when there is a collision)
    Constants drop O(2n) -> O(n) is therefore our Time Complexity

    Space Complexity: O(n) space is dependant on number if items in hash table (n)


Example:
nums = [5,2,6]
target = 7

hash map:
5:0
2:1
6:2

- Pass through list checking if 7(target) - 5(number) exists as a key in dict
- In this case it does(2)
- Return the current index we are at in the list(0) and the value of 2(1)
- [0,1] are two indices in the list whose numbers add up to 7
'''
def main():
    nums = [5, 7, 5, 15]
    target = 10
    print(twoSum(nums, target))


def twoSum(nums: list, target: int) -> list:
    numsDict = {}
    for i in range(len(nums)):
        numsDict[nums[i]] = i
    for i in range(len(nums)):
        if (target - nums[i] in numsDict and i != numsDict.get(target - nums[i])):
            return[i, numsDict.get(target - nums[i])]


main()
