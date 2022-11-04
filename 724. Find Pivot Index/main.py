

def main(nums):
    p1 = 0
    p2 = sum(nums) - nums[0]
    if p1 == p2:
        return 0

    for i in range(1, len(nums)):
        p1 += nums[i-1]
        p2 -= nums[i]
        if p1 == p2:
            return i
    return -1


nums1 = [1,2,3]
print(main(nums1))