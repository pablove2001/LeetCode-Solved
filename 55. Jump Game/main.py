class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                return False
            count = max(count-1, nums[i])
        return True
