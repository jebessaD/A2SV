class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def find_com(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            
            sum_ = 0
            for num in nums:
                sum_ += find_com(target - num)
                
            return sum_
            
        return find_com(target)
        