class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = set()
        for n in nums:
            if n in cnt:
                return True
            cnt.add(n)
        return False