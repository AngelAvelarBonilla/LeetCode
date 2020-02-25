'''
LeetCode
Difficulty: Easy
20. Valid Parentheses
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

My Solution:
    Create a faux stack using a list.
    Iterate thru each character in the string.
    If the char is an open bracket, push it's closing counterpart onto the stack
    If it is a closing bracket, check to see if the char ontop of the stack is the same, if it is pop the stack.
    If it is not, the string is invalid.

    Returns true if the stack is empty after iterating thru every character.

Complexity Analysis:
    According to LeetCode my solution had a runtime of 24ms and was faster than 90% of the Python3 solutions,
    however I feel like my solution was high inneficient and is not elegant at all. Will revisit this problem when I have a better
    understanding of Python as I am still new to this language as of 2/24/2020

Example:
    String = ({})

    Stack:
    first char: (
    Push ) onto stack

    Stack: )
    char: {
    Push } onto stack

    Stack: )}
    char: }
    Pop the stack

    Stack: )
    char: )
    Pop the stack

    Empty stack at the end therefore the string was valid

'''
def main():
    input = "()"
    print (isValid(input))


def isValid(s: str) -> bool:
    stack = []
    for char in s:

        if char == "(":
            stack.append(")")
        elif char == "[":
            stack.append("]")
        elif char == "{":
            stack.append("}")

        try:
            stack[len(stack)-1]
        except:
            return False

        if char == ")" or char == "]" or char == "}":
            if char == stack[len(stack)-1]:
                stack.pop(len(stack)-1)
            else:
                return False

    return len(stack) == 0

main()
    
