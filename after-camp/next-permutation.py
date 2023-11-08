class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=r=len(nums)-1
        while r>0 and l>0 and r>=l:
            if nums[l-1]<nums[l]:
                while r>l:
                    if(nums[r]>nums[l-1]):
                        break
                    r-=1
                nums[l-1],nums[r]=nums[r],nums[l-1]
                nums[l:]=nums[l:len(nums)][::-1]
                break
            else:
                l-=1
        if(r==len(nums)-1 and l==0):
            nums.sort()
