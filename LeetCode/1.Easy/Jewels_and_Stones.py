'''
LeetCode
Difficulty: Easy
771. Jewels and Stones
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
    Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

    The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" 
    is considered a different type of stone from "A".

My Solution:
    My Solution was to use a hashmap to store each type of jewel as a key with the value being how many times
    it appears in the stones string. 0 by default

    As we iterate thru the stones string we check to see if that stone is a key in the the hashmap
    if it is, then we increment its value by 1

    We then return the sum of all values in the hashmap

    Note: This could have easily been done using nested for loops however that would have
    been less efficient O(n^2) and harder to read than the solution below.

Complexity Analysis:
    O(n)
    We iterate thru and store J into a hasmap O(n) which has near constant look up time O(1)
    We iterate thru S O(n) and look up each character as a value in the hashmap
    O(2n) -> O(n)
    
Example:
    J = "aA"
    S = "aAAbbbb"
    We store the chars of J as keys into a Hashmap using 0 as our starting values
    a : 0
    A : 0
    We iterate thru each character in S checking to see if it exists as a char in our hashmap
    If it is increment by one
    a : 1
    A : 2
    Return the sum of all the values
    3
'''
def main():
    J = "QAZ"
    S = "qaQaazZaZAQAAzaQazzaQAZZZZaZ"
    print(numJewelsInStones(J, S))

def numJewelsInStones(J: str, S: str) -> int:
    jewels = {}

    for i in range(len(J)):
        jewels[J[i]] = 0

    for i in range(len(S)):
        if S[i] in jewels:
            jewels[S[i]] += 1

    return sum(jewels.values())

main()