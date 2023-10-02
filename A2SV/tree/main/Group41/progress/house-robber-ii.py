class Solution:
    def rob(self, nums: List[int]) -> int:

        def find_dp(arr):
            dp = [0,0]
            for num in arr:
                dp = [num + dp[1],max(dp)]
      
            return max(dp)

        return max(find_dp(nums[:-1]),find_dp(nums[1:]), nums[0] if len(nums)==1 else 0)
        


        