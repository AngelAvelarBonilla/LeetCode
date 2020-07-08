def main():
    print(isValid("[]()"))


def isValid(s: str) -> bool:
    parensDict = {"(": ")", "[": "]", "{": "}"}
    stackOfParens = []

    for char in s:
        if char in parensDict.keys():
            stackOfParens.append(parensDict[char])
        elif stackOfParens and char == stackOfParens[-1]:
            stackOfParens.pop()
        else:
            return False

    return not stackOfParens


main()
