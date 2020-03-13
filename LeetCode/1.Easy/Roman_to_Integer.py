'''
LeetCode
Difficulty: Easy
13. Roman to Integer:
    Given a roman numeral, convert it to an integer. 
    Input is guaranteed to be within the range from 1 to 3999

My Solution:

Complexity Analysis:

Example:
'''
def main():
    s = "III"
    print(romanToInt(s))
def romanToInt(s: str) -> int:
    romanNums = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    for i in range(len(s)):
        pass