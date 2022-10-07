class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        size=len(cardPoints)
        l=r=presum=ans=0
        
        while r<size:
            presum+=cardPoints[r]
            if(r-l==size-k-1):
                ans=max(ans,total-presum)
                presum-=cardPoints[l]
                l+=1
            r+=1
            
        if r-l==size: return total
        return ans
                
            