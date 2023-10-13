class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(l,r):

            if l>=r:
                return int(l==r)

            take,skip = 0,0
            if s[l] == s[r]:
                take = 2 + dp(l+1,r-1)
            else:
                skip = max(dp(l+1,r),dp(l,r-1))

            return take + skip

        return dp(0,len(s)-1)
        