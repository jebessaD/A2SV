# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=presum=0
        res=float(inf)
        while r<len(nums):
            presum+=nums[r]
            while(presum>=target):
                res=min(res,r-l+1)
                presum-=nums[l]
                l+=1
            
            r+=1
        if res==inf :return 0
        return res