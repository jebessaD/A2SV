class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        size = len(cost)

        def goUp(n):
            if n == size - 1 or n == size -2:
                return cost[n]

            if n not in memo:
                memo[n] = (goUp(n+1), goUp(n+2))

            return cost[n] + min(memo[n])

        return min(goUp(0),goUp(1))
            
            

        