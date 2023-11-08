class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1,p2 = 0,0
        while p1 < len(nums) and p2 < len(nums):

            if nums[p2]:
                nums[p1],nums[p2] = nums[p2],nums[p1]
                p1 += 1
            p2+=1


        