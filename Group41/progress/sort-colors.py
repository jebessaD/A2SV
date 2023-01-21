
#solution 1 two pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=0
        while right < len(nums):
            if nums[right] == 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right += 1
        left=right=len(nums) - 1

        while left >= 0:
            if nums[left] == 2:
                nums[left],nums[right] = nums[right],nums[left]
                right -= 1
            left -= 1

#solution 2 - bubble sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]