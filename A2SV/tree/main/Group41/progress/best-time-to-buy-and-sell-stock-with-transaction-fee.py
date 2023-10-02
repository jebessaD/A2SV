class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #top down
        @cache
        def dfs(ind,can_sell):
            if ind >= len(prices):
                return 0

            if can_sell:
                return max(prices[ind] - fee + dfs(ind + 1,False),dfs(ind + 1, True))
            else:
                return max(-prices[ind] + dfs(ind+1,True),dfs(ind + 1,False))

        return dfs(0,False)