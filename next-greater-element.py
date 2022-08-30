class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for n in nums1:
            a = nums2.index(n)
            if (a+1==len(nums2)):
                ans.append(-1)
            for i in range(a+1,len(nums2)):
                if(nums2[i]>n):
                    ans.append(nums2[i])
                    break
                if(i==len(nums2)-1):
                    ans.append(-1)
        return(ans)
               