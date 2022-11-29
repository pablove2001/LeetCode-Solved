class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        mx = 0
        for c in s:
            if c not in queue:
                queue.append(c)
                mx = max(mx, len(queue))
            else:
                while queue and queue[0] != c:
                    queue.pop(0)
                queue.pop(0)
                queue.append(c)
        
        return mx