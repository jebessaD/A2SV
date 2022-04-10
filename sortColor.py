 class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=[0]*3
        for n in nums:
            
            counter[n]+=1
        print(counter)
        a=0
        for j,i in enumerate( counter):
            for v in range(i):
                if j==0:
                    nums[v]=j
                    a+=1
                elif j==1:
                    nums[a]=j
                    a+=1
                elif j==2:
                    nums[a]=j
                    a+=1
                    
                
                
        
        