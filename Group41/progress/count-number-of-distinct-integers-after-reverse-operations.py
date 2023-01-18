class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        for num in nums_set:
            nums.append(int(str(num)[::-1]))
        return len(set(nums))
        