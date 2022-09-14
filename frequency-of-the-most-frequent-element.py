class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        presum,p1,p2=0,0,0
        ans=1
        while(p1<len(nums)):
            while(p2<len(nums) and (p2-p1)*nums[p2]<=presum+k ):
                presum+=nums[p2]
                if(p2-p1+1>ans):
                    ans=p2-p1+1
                p2+=1
            presum-=nums[p1]
            p1+=1  
        return ans