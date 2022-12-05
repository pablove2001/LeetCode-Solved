class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        n1, n2, n3 = 0, 1, 1
        for i in range(n-2):
            n1, n2, n3 = n2, n3, n3+n2+n1
        
        return n3