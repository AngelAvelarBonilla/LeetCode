def main():
    print(isUgly(8))


def isUgly(num: int) -> bool:
    uglyFactors = [2, 3, 5]

    for factor in uglyFactors:
        while num % factor == 0 and num:
            num = num / factor

    return True if num == 1 else False


main()