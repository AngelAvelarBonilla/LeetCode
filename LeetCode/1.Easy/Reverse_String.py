'''
LeetCode
Difficulty: Easy
344. Reverse String
    Write a function that reverses a string. 
    The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this 
    by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

My Solution:
    We make changes to the string n / 2 times. We drop the decimal of n /2
    because if the string has an odd number of characters and the result of n/2 has
    a remainder, then the middle character will not be swapped with anything.

    Each time we iterate we swap the characters in position i from the front and back

Complexity Analysis:
    We're only going through the whole string once and we are not allocating more space
    for another array, Thus this algorithim should be fairly efficient with a time
    complexity of O(n)

Example:
    We have an array of characters that is the string: HELLO
    There are 5 characters so we are swapping 5//2 times which is 2

    First time thru the for loop we swap chars 0 offset from the start and
    0 offset from the end in this case: H and O
    Our string is now OELLH

    Second time thru the loop we swap chars 1 offset from the start and 1
    offset from  the end: E and L
    Our string is now OLLEH

    We finished our 2 swaps which means the string is now reversed
'''
def main():
    s = ["H","I","!"]
    reverseString(s)

def reverseString(s: list) -> None:
    for i in range(len(s)//2):
        s[i],s[-(i + 1)] = s[-(i + 1)],s[i]

main()