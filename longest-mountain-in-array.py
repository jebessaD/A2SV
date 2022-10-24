# https://leetcode.com/problems/longest-mountain-in-array/submissions/
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]> arr[i+1]: #find pick 
                r=l=i
                while r<len(arr)-1 and arr[r]>arr[r+1]: # go down in right direction
                    r+=1
                while l>=1 and arr[l]>arr[l-1]: #go doen in left direction
                    l-=1
                ans=max(ans,r-l+1)
        return ans
                