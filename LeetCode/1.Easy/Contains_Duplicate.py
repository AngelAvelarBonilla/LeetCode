def main():
    print(containsDuplicate([1, 2, 3, 4]))


def containsDuplicate(nums: list) -> bool:
    setOfNums = set()
    for x in nums:
        setOfNums.add(x)
    if len(setOfNums) != len(nums):
        return True
    else:
        return False


main()

