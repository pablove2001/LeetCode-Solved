def main(nums, target):
    p1 = 0
    p2 = len(nums)-1

    if nums[p1] == target:
        return p1
    if nums[p2] == target:
        return p2
    if target < nums[p1] or target > nums[p2]:
        return -1

    while p2 - p1 > 1:
        c = int((p2-p1)/2)+p1
        #print(f'p1 = {p1}, p2 = {p2}, c = {c}')
        if nums[c] > target:
            p2 = c
        elif nums[c] < target:
            p1 = c
        else:
            return c
    return -1


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
target = 1
for i in range(-5, 20):
    print(main(nums, i))
