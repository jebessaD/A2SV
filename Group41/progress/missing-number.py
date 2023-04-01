class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = [4,2,1,3,0]
        nums.append(None)
        ind = 0
        count = 0
        while ind < len(nums):
            correct_position = nums[ind]
            if nums[ind] != ind and correct_position != None:
                nums[ind],nums[correct_position] = nums[correct_position], nums[ind]
            else:
                ind += 1

        return nums.index(None)