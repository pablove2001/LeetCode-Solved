class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                print(strs[j-1][i], strs[j][i])
                if strs[j-1][i] > strs[j][i]:
                    cnt += 1
                    break

        return cnt