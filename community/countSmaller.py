class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted = nums.copy()
        sorted.sort()
        counter=[]
        for n in nums:
            c=sorted.index(n)
            counter.append(c)
        return counter