
def main(nums):
    nums.sort(reverse=True)
    while len(nums) > 2 and nums[0] >= sum(nums[1:3]):
        nums.pop(0)
    return 0 if len(nums) < 3 else sum(nums[:3])
    



nums = [2,1,2]
print(main(nums))
