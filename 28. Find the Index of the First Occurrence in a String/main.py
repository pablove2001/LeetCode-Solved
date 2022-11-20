class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1 = 0
        p2 = len(needle)
        while p2 <= len(haystack):
            if haystack[p1:p2] == needle:
                return p1
            p1 += 1
            p2 += 1
        return -1