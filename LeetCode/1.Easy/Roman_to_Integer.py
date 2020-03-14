'''
LeetCode
Difficulty: Easy
13. Roman to Integer:
    Given a roman numeral, convert it to an integer. 
    Input is guaranteed to be within the range from 1 to 3999

My Solution:
    Iterate thru each key in the map

    While our current key is in the string we replace that occurence with an empty
    character and add the value of that key to our total

Example:
    input = XIV
    We iterate thru each key
    We reach IV first as that comes before it in the hashmap
    IV is removed from the string by replacing it with '' and its value(4) is added
    to our total

    Eventually we reach the X key in the hasmap and replace it within the string and 
    add its value to our total

    Return total
'''
def main():
    s = "III"
    print(romanToInt(s))

def romanToInt(s: str) -> int:
    total = 0
    romanNums = {
                 "IV":4,
                 "IX":9,
                 "XL":40,
                 "XC":90,
                 "CD":400,
                 "CM":900,
                 "I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000}

    for key in romanNums:
        while key in s:
            s = s.replace(key,'',1)
            total += romanNums[key]

    return total

main()