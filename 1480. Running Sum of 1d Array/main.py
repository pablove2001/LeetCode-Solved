

def main(nums):
    arr = [nums[0]]
    for i in range(1, len(nums)):
        arr.append(arr[-1]+nums[i])
    return arr

nums1 = [3,1,2,10,1]

print(main(nums1))