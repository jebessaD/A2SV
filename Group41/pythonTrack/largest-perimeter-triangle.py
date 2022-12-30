class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left=0
        while left < len(nums)-2:
            if nums[left]<nums[left+1] + nums[left+2]:
                return nums[left]+nums[left+1] + nums[left+2]
            else:
                left+=1     
        return 0