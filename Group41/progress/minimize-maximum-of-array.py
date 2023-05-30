class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        partial_sum = 0
        for i in range(len(nums)):
            partial_sum += nums[i]
            ans = max(ans , math.ceil(partial_sum / (i+1)))

        return ans



