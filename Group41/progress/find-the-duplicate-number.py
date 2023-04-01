class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            cor_pos = nums[i]-1
            if nums[cor_pos] == nums[i] and cor_pos!= i:
                return nums[i]
            elif i != cor_pos:
                nums[i],nums[cor_pos] = nums[cor_pos],nums[i]
            else:
                i += 1
        