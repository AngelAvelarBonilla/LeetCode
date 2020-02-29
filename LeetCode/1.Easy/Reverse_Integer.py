'''
LeetCode
Difficulty: Easy
7. Reverse Integer
    Given a 32-bit signed integer, reverse digits of an integer.

My Solution:
    My solution was to cast the int into a string, we then determine if the number is negative,
    If it is then we add a negative sign to our result
    Then we loop thru the string backwards adding each character to the result as long as it is not
    a '-' 
    We check to see if our result falls between the 32-bit signed integer range
    We return 0 if it doesnt, and the result if it does.

Complexity Analysis:

Example:
    -201 gets passed in. It gets casted to a string and our first character is a '-'
    This our result string which is currently "" gets '-' added to it, thus leaving us with
    "-", we then go thru the string backwards adding each character to the string
    "-1"
    "-10"
    "-102"
    The result gets casted back to an int, we check if it falls between range, and it does so we return it.
'''
def main():
    x = 153423646
    print (reverse(x))

def reverse(x: int) -> int:
    x = str(x)
    result = ''

    if x[0] == '-':
        result += '-'

    for i in range(len(x)):
        if x[-(i+1)] != '-':
            result += x[-(i + 1)]

    result = int(result)
    if result > 2**31 - 1 or result < -2**31:
        return 0
    else:
        return result


main()