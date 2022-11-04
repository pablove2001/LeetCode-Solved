

def main(nums):
    p1 = 0
    p2 = sum(nums)
    if p1 == p2:
        return 0

    for i in range(0, len(nums)):
        p1 += nums[0:i]
        p2 -= 
        if sum(nums[0:i]) == sum(nums[i+1:len(nums)]):
            return i
    return -1


nums1 = [2,1,-1]
print(main(nums1))