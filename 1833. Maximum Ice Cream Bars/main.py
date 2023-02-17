class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        heapify(costs)
        res = 0

        lend = len(costs)

        while res < lend:
            c = heappop(costs)
            if c > coins:
                break
            coins -= c
            res += 1

        return res
