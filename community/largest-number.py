class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                conc=str(nums[j]) + str(nums[j+1])
                conc2=str(nums[j+1]) + str(nums[j])        
                if(int(conc)<int(conc2)):
                    c=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=c
        ans = ''.join([str(elem) for elem in nums])
        
        return(str(int(ans)))
            
        
        