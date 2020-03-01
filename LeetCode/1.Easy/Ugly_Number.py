'''
LeetCode
Difficulty: Easy
263. Ugly Number

My Solution:
    We divide by each possible factor (2, 3, 5) sequentially until we can no longer evenly divide it.
    After going thru each factor if the number is truly ugly the remainder should be 1.

Complexity Analysis:

Example:
'''
def main():
    x = 1
    print(isUgly(x))

def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a

def isUgly(num: int) -> bool:
    num = maxDivide(num,2)
    num = maxDivide(num,3)
    num = maxDivide(num,5)
    return True if num == 1 else False

main()
