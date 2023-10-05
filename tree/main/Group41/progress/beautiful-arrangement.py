class Solution:
    def countArrangement(self, n: int) -> int:
#not 
        @cache
        def dfs(i, mask):
            if i > n:
                return 1
            ans = 0
            for j in range(1, n+1):
                if (i % j == 0 or j % i == 0) and not (mask >> j & 1):
                    ans += dfs(i+1, mask | 1 << j)
            return ans
        return dfs(1, 0)