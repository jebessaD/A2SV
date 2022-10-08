# https://leetcode.com/problems/subarray-sum-equals-k/submissions/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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