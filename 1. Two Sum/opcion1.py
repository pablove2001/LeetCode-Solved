

def main(nums, target):
    leng = len(nums)
    for i in range(leng):
        for j in range(i+1, leng):
            if target == (nums[i] + nums[j]):
                return [i, j]
    return


nums1 = [3,4,6,2]
target1 = 9

print(main(nums1, target1))