def main():
    print(reverse(-21))


def reverse(x: int) -> int:
    isNegative = False

    if x < 0:
        isNegative = True
        x = -x

    x = int(str(x)[::-1])
    if x > 2**31 - 1:
        return 0

    if isNegative:
        x = -x

    return x


main()
