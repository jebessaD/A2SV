class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=r=ans=total=0
        while r<len(arr):
            total+=arr[r]
            if(r-l==k-1):
                if(total >=k*threshold):
                    ans+=1
                total-=arr[l]
                l+=1
            r+=1
        return ans