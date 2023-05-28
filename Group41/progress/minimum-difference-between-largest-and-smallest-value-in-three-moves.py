class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 4:
            return 0

        ans = nums[-1] - nums[0]
        for i in range(1,5):
            ans = min(ans,nums[-i] - nums[4-i])

        return ans

        
