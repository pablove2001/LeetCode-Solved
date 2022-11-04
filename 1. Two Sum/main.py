def main(nums, target):
    pointer1 = 0
    pointer2 = len(nums)-1
    old = nums.copy()
    nums.sort()

    while pointer1 < pointer2:
        suma = nums[pointer1] + nums[pointer2]
        if suma > target:
            pointer2-=1
        elif suma < target:
            pointer1+=1
        else: 
            toFind = [nums[pointer1], nums[pointer2]]
            return1 = -1
            for i in range(0, len(old)):
                if old[i] in toFind:
                    if return1 == -1:
                        return1 = i
                    else:
                        return [return1, i]


            return [pointer1, pointer2]
    return




nums1 = [5,6, 3,2]
target1 = 9

print(main(nums1, target1))