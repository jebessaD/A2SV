class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=r=ans=0
        zero=set()
        
        while r<len(nums):
            if nums[r]==0:
                zero.add(r)
            if len(zero)>1:
                ans=max(ans,r-l-1) 
                min_index =min(zero)
                l=min_index+1
                zero.remove(min_index)
            r+=1
        return max(ans,r-l-1)
                  