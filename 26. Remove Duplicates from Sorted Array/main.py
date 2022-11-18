class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[cnt] = nums[i+1]
                cnt += 1
        return cnt