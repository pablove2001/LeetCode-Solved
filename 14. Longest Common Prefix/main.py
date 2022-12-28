class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenW = min(len(i) for i in strs)
        res = ''

        for i in range(lenW):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return res
            res += strs[0][i]
            
        return res