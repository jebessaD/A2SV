class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        k%=len(nums)
        l,r=0,k-1     
        while l<r:
            nums[r],nums[l]=nums[l],nums[r]
            r-=1
            l+=1
        l,r=k,len(nums)-1
        while l<r:
            nums[r],nums[l]=nums[l],nums[r]
            r-=1
            l+=1
            