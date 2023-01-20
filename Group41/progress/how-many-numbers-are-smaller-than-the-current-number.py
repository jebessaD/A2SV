class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        position = sorted(nums)
        ans=[]
        for num in nums:
            ans.append(position.index(num))
        return ans