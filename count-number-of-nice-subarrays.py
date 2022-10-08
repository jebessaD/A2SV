# https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums=list(map(lambda num: num %2,nums))
        ans=presum=0
        store={}
        for r in range(len(nums)):
            if(presum-k in store):
                ans+=store[presum-k]
            if presum in store: store[presum]+=1
            else: store[presum]=1
            presum+=nums[r]
            
        if(presum-k in store):
                ans+=store[presum-k]   
        return ans