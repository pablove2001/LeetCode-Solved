class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        return max(maxlength(nums), maxlength(nums[::-1]))


def maxlength(nums):
    mx = 0
    p = True
    c = 0

    for n in nums:
        c += 1
        if n == 0:
            c = 0
            p = True
            continue

        if n < 0:
            p = not p
        if p:
            mx = max(c, mx)

    return mx
