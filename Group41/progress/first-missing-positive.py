class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        while i < n:
            corr_pos = nums[i] - 1
            if 0 <= corr_pos < n and nums[corr_pos] != nums[i]:
                nums[corr_pos],nums[i] = nums[i],nums[corr_pos]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n + 1
       