class Solution:
    def isHappy(self, n: int) -> bool:
        path = set()
        while n != 1:
            path.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            if n in path:
                return False
        return True
