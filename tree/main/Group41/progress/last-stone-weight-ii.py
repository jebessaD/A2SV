class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = math.ceil(total/2)
        @cache
        def dp(sum_,i):

            if sum_ >= target or i >= len(stones):
                return abs(sum_ - (total - sum_))

            return min(dp(sum_+ stones[i], i+1), dp(sum_,i+1))

        return dp(0,0)

        