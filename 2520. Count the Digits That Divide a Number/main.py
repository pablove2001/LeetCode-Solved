class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        div = str(num)

        for i in div:
            if num % int(i) == 0:
                res += 1

        return res
