class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        index={}
        ans=r=l=0
        while r<len(fruits):
            index[fruits[r]]=r
            if(len(index)<=2):
                r+=1
            else:
                ans=max(r-l,ans)
                minval=min(index.values())
                del index[fruits[minval]]
                l=minval+1 
        ans=max(r-l,ans)
        return ans
                