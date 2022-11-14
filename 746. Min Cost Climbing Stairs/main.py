class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            arr.append(min(arr[i-1], arr[i-2]) + cost[i])
        return min(arr[-1], arr[-2])
