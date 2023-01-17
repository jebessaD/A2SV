class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        premul=1
        ans=[]
        for n in nums:
            ans.append(premul)
            premul*=n      
        
        premul=1   
        for i,n in enumerate(reversed(nums)):
            ans[len(nums)-i-1] *=premul
            premul*=n
            
        return ans
            