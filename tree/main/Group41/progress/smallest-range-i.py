class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        curr_diff = max(nums) - min(nums)
        
        if curr_diff > k*2:
            return curr_diff - 2*k
        
        return 0