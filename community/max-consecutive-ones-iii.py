# https://leetcode.com/problems/max-consecutive-ones-iii/submissions/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=l=r=0
        zeros=deque()
        while r<len(nums):
            if(nums[r]==0):
                zeros.append(r)
            if(len(zeros)>k):
                ans=max(r-l,ans)
                l=zeros.popleft()+1
                
            r+=1
        return max(ans,r-l)
        