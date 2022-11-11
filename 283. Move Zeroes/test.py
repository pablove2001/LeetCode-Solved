def main(nums):
    i = 0
    f = len(nums)
    while i < f:
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            f-=1
        else:
            i+=1
    return nums

nums = [0,1,0,3,12]
print(main(nums))