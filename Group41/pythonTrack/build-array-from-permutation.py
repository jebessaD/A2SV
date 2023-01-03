class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for ind in range(len(nums)):
            ans[ind]=nums[nums[ind]]

        return ans