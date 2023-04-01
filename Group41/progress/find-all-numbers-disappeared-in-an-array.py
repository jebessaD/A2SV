class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            cor_pos = nums[i]-1
            if i != cor_pos and nums[cor_pos] != nums[i]:
                nums[i],nums[cor_pos] = nums[cor_pos],nums[i]
            else:
                i += 1
        ans = [i + 1 for i in range(n) if i != nums[i] - 1 ]
        return ans