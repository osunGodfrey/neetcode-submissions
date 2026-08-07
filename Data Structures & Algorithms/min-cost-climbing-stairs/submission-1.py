class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0] * len(cost)
        for i in range(len(cost)):
            # print(mincost)
            if i == 0:
                mincost[i] = cost[i]
                continue
            if i == 1:
                mincost[i] = min(mincost[i - 1] + cost[i], cost[i])
                continue
            mincost[i] = min(mincost[i - 1] + cost[i], mincost[i - 2] + cost[i])
        # print(mincost)
        return min(mincost[len(cost) - 1], mincost[len(cost) - 2])

        