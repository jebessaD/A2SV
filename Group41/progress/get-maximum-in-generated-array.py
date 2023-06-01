class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        
        def getMax(i):
            if i == 0 or i == 1:
                return i

            if i not in memo and i%2 == 0:
                memo[i] = getMax(i//2)

            elif i not in memo and i%2 != 0:
                memo[i] = getMax(i//2) + getMax(i//2 + 1)

            return memo[i]
        
        ans = 0
        for i in range(1,n+1):
            ans = max(ans,getMax(i))
        return ans