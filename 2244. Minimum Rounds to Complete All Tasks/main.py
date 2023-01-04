class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        a = Counter(tasks)
        res = 0

        for i in a.values():
            if i <= 1:
                return -1

            res += int((i+2)/3)

        return res
