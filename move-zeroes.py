class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=r=0
        while(l<len(nums) and r<len(nums)):
            if(nums[r] !=0):
                print(l,r)
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
            r+=1
            