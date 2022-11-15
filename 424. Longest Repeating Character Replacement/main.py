class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        mx = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1

            if r-l - max(d.values()) < k:
                mx = max(r-l+1, mx)
            else:
                d[s[l]] -= 1
                l += 1
        return mx