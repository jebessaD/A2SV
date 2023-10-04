class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(curr_size,clip_size):
            if curr_size > n:
                return float('inf')

            if curr_size == n:
                return 0

            path1 = 1 + dp(curr_size + clip_size,clip_size)
            path2 = 2 + dp(curr_size * 2, curr_size)

            return min(path1,path2)

        return 1 + dp(1,1) if n > 1 else 0      