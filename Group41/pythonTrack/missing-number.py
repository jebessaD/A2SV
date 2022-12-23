class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set=set(nums)
        all_range=[i for i in range(len(nums)+1)]
        ans= set(all_range).difference(nums_set)
        return ans.pop()
        