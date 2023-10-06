class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        nums = [(score,age) for score,age in zip(scores,ages)]
        
        nums.sort()
        dp = [nums[i][0] for i in range(len(nums))]

        for curr in range(len(nums)):
            for prev in range(curr):
                if nums[prev][1] <= nums[curr][1]:
                    dp[curr] = max(nums[curr][0] + dp[prev],dp[curr])

        return max(dp)
        