class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size=len(nums)
        arr=[]
        for i in range(size//2):
            a=nums[i]+nums[size-1-i]
            arr.append(a)
            
        return(max(arr))
        