class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        res = [False]*(len(s)+1)
        res[0] = True

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if res[i] and s[i:j] in words:
                    res[j] = True
                    
        return res[-1]