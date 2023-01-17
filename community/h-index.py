class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans=0     
        for i in range(1,len(citations)+1):
            if(i<=citations[i-1]):
                ans=i 
        return ans