class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(ind,time):
            if ind == len(satisfaction):
                return 0

            return max((time * satisfaction[ind]) + dp(ind+1,time+1), dp(ind+1,time))

        return dp(0,1)

        

