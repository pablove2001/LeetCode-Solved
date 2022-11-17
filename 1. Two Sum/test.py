def main(nums, target):
    nMap = {}
    for i in range(len(nums)):
        if target - nums[i] in nMap:
            return [nMap[target - nums[i]], i]
        else:
            nMap[nums[i]] = i

    pass