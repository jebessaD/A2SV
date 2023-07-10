class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(coin,memo):
            if coin < 0:
                return float("inf")
            if coin == 0:
                return 0

            if coin in memo:
                return memo[coin]
            
            memo[coin] =  min(dp(coin-c, memo) + 1 for c in coins)
            return memo[coin]

        ans = dp(amount,{})
        if ans == float("inf"):
            return -1
        return ans
        