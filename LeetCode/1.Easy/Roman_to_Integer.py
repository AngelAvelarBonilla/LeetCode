def main():
    print(romanToInt("MCMXCIV"))


def romanToInt(s: str) -> int:
    total = 0
    romanDict = {"IV": 4,
                 "IX": 9,
                 "XL": 40,
                 "XC": 90,
                 "CD": 400,
                 "CM": 900,
                 "I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000,
                 }

    for key, value in romanDict.items():
        while key in s:
            s = s.replace(key, '', 1)
            total += value
    return total

main()