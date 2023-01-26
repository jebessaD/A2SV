class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swapper(nums, left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

        k= k % len(nums)        
        swapper(nums , 0 , len(nums)- k - 1)
        swapper(nums , len(nums)-k, len(nums)- 1)
        swapper(nums , 0 ,len(nums)- 1)


        

