from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        que=deque()
        length=0
        mini=nums[0]
        maxi=nums[0]
        for num in nums:
            if(num>maxi):
                maxi=num
            elif(num<mini):
                mini=num
            que.append(num)
            if (abs(maxi-mini)>limit):
                a=que.popleft()
                if(a==mini):
                    mini=min(que)
                if(a==maxi):
                    maxi=max(que)
                
            if(length<len(que)):
                length=len(que)
        return(length)