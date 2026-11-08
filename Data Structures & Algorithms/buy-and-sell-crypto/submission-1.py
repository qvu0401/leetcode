class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0

        for r in range(1, len(prices)):
            if prices[r] - prices[l] < 1:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > ans:
                    ans = profit
                
        return ans
        