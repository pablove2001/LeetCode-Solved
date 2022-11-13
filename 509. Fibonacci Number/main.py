class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        n1, n2 = 0, 1
        for i in range(n-1):
            n1, n2 = n2, n2+n1
        return n2