class Solution:
    def numSquares(self, n: int) -> int:
        squares = [ i * i for i in range(1, int(math.sqrt(n)) + 1)]
        cnt = 0
        nums = [n]

        while nums:
            remain = set()
            cnt += 1
            for num in nums:
                for sq in squares:
                    if sq == num:
                        return cnt
                    if num < sq:
                        break
                    remain.add(num - sq)
            nums = list(remain)