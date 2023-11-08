class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        ans = 0
        for price in prices:
            ans = max(ans,price - curr_min)
            curr_min = min(curr_min, price)

        return ans




        