class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_min = prices[0]
        s_max = prices[0]
        profit = max(0, s_max - b_min)
        for p in prices:
            if min(b_min, p) == b_min:
                s_max = max(s_max, p)
                profit = max(profit, s_max - b_min)
            else:
                s_max = p
                b_min = min(b_min, p)
                profit = max(profit, s_max - b_min)
            # print(b_min, s_max)
        return profit