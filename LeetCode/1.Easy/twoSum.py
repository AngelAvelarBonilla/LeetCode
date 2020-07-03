def main():
    print(twoSum([4, 3, 2], 6))


def twoSum(nums: list, target: int) -> list:
    numsDict = {}
    for i in range(len(nums)):
        numsDict[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in numsDict and i != numsDict.get(target - nums[i]):
            return [i, numsDict.get(target - nums[i])]




main()
