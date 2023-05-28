class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float(inf)
        second = float(inf)

        for num in nums:
            first = min(first,num)
            if num > second:
                return True
            if num > first:
                second = num
                
        return False

        