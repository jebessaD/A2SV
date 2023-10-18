class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        # 
        res, score = 0, sys.maxsize
        for n in nums:
            score &= n
            if not score:
                res += 1
                score = sys.maxsize
                
        return max(1, res)