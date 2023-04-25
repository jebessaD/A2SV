class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        ans = 0
        d = 2
        while d * d <= n:
            if n % d == 0:
                ans += d
                n = n // d
            else:
                d+=1

        ans += n
        return ans
        