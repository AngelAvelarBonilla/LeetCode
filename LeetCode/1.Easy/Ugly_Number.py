'''
LeetCode
Difficulty: Easy
263. Ugly Number

My Solution:
    We divide by each possible factor (2, 3, 5) sequentially until we can no longer evenly divide it.
    After going thru each factor if the number is truly ugly the remainder should be 1, if it is not then
    the number has another prime factor and as a result we can determine that it is not ugly.

Example:
    Our input is 300. We divide by two until we can longer evenly divide by it.
    We now have 75, we divide by 3 so now we have 25, from here we can divide by 5 until
    we are left with 1. Thus 300 is an ugly number. Result: True
'''
def main():
    x = 300
    print(isUgly(x))

def maxDivide(a: int, b: int):
    while a % b == 0 and a !=0:
        a = a / b
    return a

def isUgly(num: int) -> bool:
    num = maxDivide(num,2)
    num = maxDivide(num,3)
    num = maxDivide(num,5)
    return True if num == 1 else False

main()
