def main(nums, target):
    pointer1 = 0
    pointer2 = len(nums)-1

    while pointer1 < pointer2:
        suma = nums[pointer1] + nums[pointer2]
        if suma > target:
            pointer2-=1
        elif suma < target:
            pointer1+=1
        else: 
            return [pointer1, pointer2]
    return


nums1 = [6,3,4,2]
target1 = 9

print(main(nums1, target1))