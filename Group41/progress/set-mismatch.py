class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            cor_pos = nums[i]-1
            if nums[cor_pos] == nums[i] and cor_pos!= i:
                ans = [nums[i],i+1]
                i+=1
            elif i != cor_pos:
                nums[i],nums[cor_pos] = nums[cor_pos],nums[i]
            else:
                i += 1

        return ans
        